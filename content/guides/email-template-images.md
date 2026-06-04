---
title: "Embed Images in Email Templates"
description: "Upload images from within the email template editor and embed them directly in your email body with permanent, token-free URLs that work in any email client."
slug: "email-template-images"
type: "guides"
product_area: "Communication"
sub_area: "Email"
audience: ["admin"]
tags: ["email", "communication", "templates", "images", "upload"]
status: "published"
source_legacy_path: ""
source_language: "en"
needs_screenshot_replacement: false
last_converted: "2026-06-04"
related_articles: ["message-templates", "dynamic-tags", "sending-email-sms"]
---

# Embed Images in Email Templates

You can now upload images directly inside the email template editor and embed them in your email body. Uploaded images get permanent URLs — they will display correctly in recipients' inboxes indefinitely, not just while a session or temporary link is active.

## Uploading an image

1. Go to **Communication → Templates** and open or create an email template.
2. In the rich-text editor toolbar, click the **Insert Image** button (image icon).
3. Click **Upload** and choose an image file from your computer.
4. The image is uploaded immediately and inserted at your cursor position.

### Supported formats

| Format | Extension |
|---|---|
| JPEG | .jpg / .jpeg |
| PNG | .png |
| GIF | .gif |
| WebP | .webp |

Maximum file size: **5 MB per image**.

### What you get

Uploaded images receive a **permanent, public URL** (for example: `https://[storage].blob.core.windows.net/email-template-images/[your-company]/email_image/[unique-id].jpg`). This URL:

- Contains **no expiry date** or security token.
- Can be safely embedded in sent emails — recipients see the image months or years after you send it.
- Is **unique per upload** — uploading the same image file twice creates two independent URLs, so changing one image in one template does not affect other templates that reference a different upload of that image.

## Role requirement

Only users with the **Edit courses** permission can upload images to email templates. Users who can only edit template text but lack this permission will not see the image upload button.

## Tips

- Keep images under 5 MB to avoid upload errors.
- Use PNG for logos or graphics with transparency.
- JPEG works best for photos.
- After uploading, you can resize the image in the editor without affecting the stored original.
