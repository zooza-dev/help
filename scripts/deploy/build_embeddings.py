"""Build Gemini embeddings from knowledge base JSONL files and upload to GCS.

Reads canonical.jsonl + faq.jsonl from build/exports/agent/,
generates embeddings using Gemini embedding API, and uploads
embeddings.npy + records.json to a GCS bucket.

Usage:
    python scripts/deploy/build_embeddings.py

Env vars:
    GEMINI_API_KEY          - Gemini API key
    KB_GCS_BUCKET           - GCS bucket name (default: zooza-kb-embeddings)
    KB_EXPORTS_DIR          - Path to agent exports (default: build/exports/agent)
"""

import json
import logging
import os
import sys
from pathlib import Path

import numpy as np
from google import genai
from google.cloud import storage

logging.basicConfig(level=logging.INFO, format="%(levelname)s: %(message)s")
logger = logging.getLogger(__name__)

BATCH_SIZE = 100
EMBEDDING_MODEL = "gemini-embedding-001"


def load_records(exports_dir: Path) -> list[dict]:
    """Load all records from canonical.jsonl and faq.jsonl."""
    records = []
    for name in ("canonical.jsonl", "faq.jsonl"):
        path = exports_dir / name
        if not path.exists():
            logger.warning("File not found, skipping: %s", path)
            continue
        with open(path, "r", encoding="utf-8") as f:
            for line in f:
                line = line.strip()
                if line:
                    records.append(json.loads(line))
    return records


def build_embeddings(records: list[dict], api_key: str) -> np.ndarray:
    """Generate embeddings for all records using Gemini API in batches."""
    client = genai.Client(api_key=api_key)
    texts = [r.get("text", "") for r in records]
    all_embeddings = []

    for i in range(0, len(texts), BATCH_SIZE):
        batch = texts[i : i + BATCH_SIZE]
        logger.info("Embedding batch %d-%d of %d...", i + 1, min(i + BATCH_SIZE, len(texts)), len(texts))
        result = client.models.embed_content(
            model=EMBEDDING_MODEL,
            contents=batch,
        )
        for embedding in result.embeddings:
            all_embeddings.append(embedding.values)

    return np.array(all_embeddings, dtype=np.float32)


def upload_to_gcs(bucket_name: str, embeddings: np.ndarray, records: list[dict]):
    """Upload embeddings.npy and records.json to GCS."""
    client = storage.Client()
    bucket = client.bucket(bucket_name)

    # Upload embeddings.npy
    emb_path = "/tmp/embeddings.npy"
    np.save(emb_path, embeddings)
    blob = bucket.blob("embeddings.npy")
    blob.upload_from_filename(emb_path)
    logger.info("Uploaded embeddings.npy (%s)", blob.size)

    # Upload records.json (only fields needed for retrieval)
    slim_records = [
        {
            "title": r.get("title", ""),
            "heading_path": r.get("heading_path", ""),
            "text": r.get("text", ""),
            "url": r.get("url", ""),
            "product_area": r.get("product_area", ""),
        }
        for r in records
    ]
    rec_path = "/tmp/records.json"
    with open(rec_path, "w", encoding="utf-8") as f:
        json.dump(slim_records, f, ensure_ascii=False)
    blob = bucket.blob("records.json")
    blob.upload_from_filename(rec_path)
    logger.info("Uploaded records.json (%s)", blob.size)


def main():
    api_key = os.environ.get("GEMINI_API_KEY")
    if not api_key:
        logger.error("GEMINI_API_KEY environment variable is required")
        sys.exit(1)

    bucket_name = os.environ.get("KB_GCS_BUCKET", "zooza-kb-embeddings")
    exports_dir = Path(os.environ.get("KB_EXPORTS_DIR", "build/exports/agent"))

    if not exports_dir.exists():
        logger.error("Exports directory not found: %s", exports_dir)
        sys.exit(1)

    records = load_records(exports_dir)
    if not records:
        logger.error("No records loaded from %s", exports_dir)
        sys.exit(1)

    logger.info("Loaded %d records", len(records))

    embeddings = build_embeddings(records, api_key)
    logger.info("Generated embeddings: shape %s", embeddings.shape)

    upload_to_gcs(bucket_name, embeddings, records)
    logger.info("Embedded %d chunks, uploaded to GCS bucket '%s'", len(records), bucket_name)


if __name__ == "__main__":
    main()