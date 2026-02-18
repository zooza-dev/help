---
title: "Smartbill - invoice management"
slug: "smartbill-invoices"
type: "setup"
product_area: "Payments"
sub_area: ""
audience: ["admin"]
tags: []
status: "published"
source_legacy_path: "legacy/0101_Welcome to Zooza.html"
source_language: "en"
needs_screenshot_replacement: false
last_converted: "2026-02-11"
intercom_id: 13728879
intercom_sync: true
---

# Smartbill - invoice management

Integration to the Smartbill billing system used in Romania.

[Program Facturare Online | Gestiune si Contabilitate | SmartBill](https://www.smartbill.ro/)

![Screenshot](../../assets/images/blocks-creation-07.png)

Connection to the service allows you to create invoices in the direction of Zooza – Smartbill.

## Functioning of the invoice management process and billing profiles when connected

1. The number of invoices issued depends on the prepaid package in Smartbill
2. VAT settings are pulled from Smartbill towards Zooza
3. The number series for invoices is set in Smartbill
4. Already created invoice can only be changed or deleted in Smartbill, no back-synchronization is possible – after editing an invoice in Smartbill, the current form of the invoice is not pulled into Zooza, Zooza communicates this directly on the invoice by flag/notice
5. Invoice data displayed in the invoice is set in Smartbill
6. Invoice data that is sent in communication with the client and in the client profile is set in Zooza

## Smartbill link – step by step

1. In Zooza, select Billing System – Smartbill along with:
2. Smartbill email address
3. Token that you find in SmartbillSection My account – Integrations – API
 ![Screenshot](../../assets/images/smartbill-invoices-02.png)


Choose whether you want automatic generation of invoices or you will manually generate invoices per booking

![Screenshot](../../assets/images/smartbill-invoices-03.png)

Set up Billing profile/s for communication from Zooza
Link your billing profile to the GoCardless app for automatic payment pairing - [Billing and invoicing](billing-and-invoicing.md)
Set the number series for invoices in Smartbill


![Screenshot](../../assets/images/smartbill-invoices-04.png)


In the billing profile detail in Zooza, select the number series that will be used for the billing profile


![Screenshot](../../assets/images/smartbill-invoices-05.png)


Set VAT levels in Smartbill
In the VAT levels settings section of Zooza, select from the options how to apply VAT levels and click on the synchronize option so that the levels are properly tightened


![Screenshot](../../assets/images/smartbill-invoices-06.png)
