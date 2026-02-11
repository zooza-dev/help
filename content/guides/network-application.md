---
title: "Network Application"
slug: "network-application"
type: "guides"
product_area: "Settings"
sub_area: ""
audience: ["admin"]
tags: []
status: "published"
source_legacy_path: "legacy/0107_Welcome to Zooza.html"
source_language: "en"
needs_screenshot_replacement: false
last_converted: "2026-02-11"
---

# Network Application

The Network Application is a centralized reporting and management platform designed to help franchisors monitor and oversee their entire franchise network. It offers comprehensive visibility into key performance metrics such as enrollments, payments, revenue, and cancellations.

These metrics can be analyzed across various dimensions—by franchise company, location, product or specific time periods—enabling deep, actionable insights through intuitive drill-down capabilities.

![Screenshot](../../assets/images/customizing-widgets-01.png)

A key strength of the application is its customizability. The franchisor has full control to:

1. Define and manage the list of companies included in the network
2. Standardize and assign product codes that unify course tracking across the network
3. Monitor the progress and performance of courses and offerings throughout all franchise branches

This application is designed to support strategic decision-making, operational oversight, and consistency across the franchise network through accurate, real-time reporting and flexible configuration.

## Reports


The reporting dashboard provides clear and comprehensive insights into key operational metrics such as enrollments, payments, revenue, and cancellations. These reports are fully interactive and support analysis across multiple dimensions—by franchise company, product, physical location (place), and time period—offering powerful drill-down capabilities for deeper business insights.


To support different organizational perspectives, the dashboard includes two toggle modes:

1. Companies Mode: Metrics are aggregated by individual franchise companies.
2. Places Mode: Metrics are aggregated by franchise locations (places)


All charts and metrics dynamically adjust based on the selected mode, allowing users to analyze performance from different organizational perspectives.

## Metrics Overview


Metrics are divided into 3 main groups:

1. Enrollments
2. Payments
3. Sessions

## Scope of metrics

### Period


Most metrics are calculated as cumulative monthly totals and saved per
period. During the current month, the period end date is always treated
as T-1 (the day before the report run). Some metrics (like enrollments
or cancellations) reflect the current state at run time to show
up-to-date values for all running classes.

### Running classes


Defined as classes of the following types:

1. Lead Collection
2. Fixed Period that has not started yet
3. Fixed Period that is ongoing

## Enrollments

### New Enrollments


The number of registrations created within the selected period, aggregated across all dimensions (e.g. product, company, place).

### Enrollments

 The number of active clients with registration status "Registered" as of the current run date (T-1). For broader date ranges, this is shown as an average across the selected periods.

![Screenshot](../../assets/images/client-import-01.png)

Note: Early in a new period, you may see only a few New Enrollments, but the total Enrollments remains high due to ongoing registrations from earlier periods.

### Unpaid Enrollments

Counts the number of enrollments with unpaid debt, whether for a currently running class or one that hasn’t started yet. Includes registrations still within their payment due window.


### Cancellations


Total number of enrollments marked as "Cancelled" as of the latest available data (T-1). For broader date ranges, this is shown as an average across the selected periods.

### Ended


Number of enrollments that have completed all sessions and ended successfully within the selected period.

## Payments

### Received Payments


The total value of credit-based payments received during the selected period. Over larger date ranges (e.g. quarters), the value is cumulative.

![Screenshot](../../assets/images/client-import-01.png)

Note: The value can occasionally be negative if the sum of corrections on a given day exceeds newly received payments.

### Net Revenue

Net Revenue represents the actual earned revenue within the selected period. It is calculated by adjusting the total received payments to account for total debt, granted discounts and issued refunds. This metric provides a more accurate reflection of real income by removing expected but unrealized or reduced revenue elements.

![Screenshot](../../assets/images/blocks-creation-07.png)

Net Revenue = Received payments - Debt - Discounts - Refunds.

### Unpaid Debt


Outstanding financial obligations tied to enrollments — either for classes already in progress or yet to start.

### Royalties


A network-specific fee calculated according to the franchisor’s defined rules. Each network may use a different formula or basis for royalty calculation.

## Sessions

### Sessions


Cumulative number of sessions scheduled during the selected period.

### Sessions with attendance


Total sessions that have recorded either attendance or public session note.

### Instructors

The number of unique instructors assigned to sessions within the selected period.

![Screenshot](../../assets/images/client-import-01.png)

Note: This metric excludes sessions where the instructor is yet to be decided.
