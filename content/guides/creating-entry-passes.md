---
title: "Creating entry passes"
slug: "creating-entry-passes"
type: "guides"
product_area: "Orders"
sub_area: ""
audience: ["admin"]
tags: ["entry pass", "credit pass", "prepaid credit", "pay-as-you-go"]
status: "published"
source_legacy_path: ""
source_language: "en"
needs_screenshot_replacement: true
last_converted: "2026-02-15"
intercom_id: 13738687
intercom_sync: false
---

# Creating entry passes

Entry passes let clients prepay for a set number of sessions or a credit amount, which is then redeemed each time they book a session in a Pay-as-you-go programme. Entry passes are optional — without them, clients simply pay per session.

## Entry pass vs Prepaid credit

Zooza supports two types of prepaid products:

- **Entry pass** — A visits-based pass. The client purchases a fixed number of entries (e.g. 10 sessions). Each time they book a session, one entry is deducted.
- **Prepaid credit** — A money-based pass. The client purchases a credit amount (e.g. 50 EUR). Each time they book a session, the session price is deducted from their credit balance.

Both types work the same way in the booking flow. Choose based on whether you want to sell by number of visits or by monetary value.

## Step-by-step: Create an entry pass product

1. Go to **Products** → **Create New Product** → Create.

   ![Create new product](../../assets/images/entry-pass-create-product.png "Products — Create new product form")

2. Enter the **credit value**, configure **payment methods** (online payment, bank transfer, cash, etc.) and save.

   ![Credit value and payment config](../../assets/images/entry-pass-credit-value-config.png "Product credit value and payment method settings")

3. Go to **Items for sale** → click **Add**.

   ![Items for sale](../../assets/images/entry-pass-items-for-sale.png "Items for sale section")

   ![Add item](../../assets/images/entry-pass-add-item.png "Add new item dialog")
4. Select **Entry Pass** as the item type.
5. Set the **value** (number of entries or credit amount), **validity period**, **price**, and whether the item is **mandatory**.
6. To offer a discount, set the price lower than the value (e.g. 10 entries for 80 EUR instead of 100 EUR).

   ![Discount pricing](../../assets/images/entry-pass-discount-pricing.png "Entry pass with discounted price")
7. Click **Continue** → **Start and Continue**.
8. Add a **description** and **notification template** if needed.

   ![Description and template](../../assets/images/entry-pass-description-template.png "Product description and notification template settings")




## Assign pass to a class

After creating the entry pass product, assign it to the relevant programme or class.

1. Go to the **Programme** → **Class** → **Select Product**.

   ![Assign product to class](../../assets/images/entry-pass-assign-to-class.png "Class settings — Select Product")

2. Choose the entry pass product you created.

   ![Select entry pass product](../../assets/images/entry-pass-select-product.png "Product selection dialog")
3. Click **Save**.

You can assign multiple pass types to the same class. For example, you might offer both a 5-session pass and a 10-session pass.

### Product settings per class

For each assigned product, you can configure where it appears:

- **Profile availability** — The pass is available for purchase in the client's profile after booking.

  ![Profile availability setting](../../assets/images/entry-pass-profile-availability.png "Entry pass available in client profile")

- **Booking form availability** — The pass is available during the booking/booking process.

  ![Booking form availability setting](../../assets/images/entry-pass-booking-form-availability.png "Entry pass available in booking form")

## Two-product setup for dual availability

There is an important limitation: a single product cannot be both mandatory (shown in the client profile) and optional (shown in the booking form) at the same time.

To offer the same entry pass in both locations, create two separate products:

1. **Mandatory product** — Set as mandatory. This makes it available in the client's profile (under Benefits).
2. **Optional product** — Set as optional. This makes it available in the booking form during booking.

Both products should have the same value and price. The only difference is the mandatory/optional setting.
![Dual product setup example](../../assets/images/entry-pass-dual-product-setup.png "Two products — mandatory for profile and optional for booking form")

### Example: 5 EUR and 10 EUR passes

To offer two pass values (5 EUR and 10 EUR) in both the profile and the booking form:

1. Create a **5 EUR mandatory product** (available in profile).
2. Create a **10 EUR mandatory product** (available in profile).
3. Create a Credit Pass Entry Options (**5 EUR optional product** and **10 EUR optional product**) (available in booking form).

You can also create a third product as a booking form bundle** that combines multiple pass options into one offering during the booking flow.

## Client perspective

After registering for a Pay-as-you-go programme, clients can:

1. Purchase an entry pass from their profile (under **Orders** and in the detail of a booking).
2. See their credit balance or remaining entries on their profile home page.
3. Book sessions — the pass is automatically redeemed when they book.
4. If they unregister from a session, the entry or credit is returned.

For a detailed walkthrough of how clients see and use entry passes, see [Entry pass — client view](entry-pass-client-view.md).

## Related guides

- [Pay-as-you-go programme](pay-as-you-go-programme.md) — How to set up the programme type that uses entry passes.
- [Linked classes](linked-classes.md) — Use one entry pass across multiple linked classes.
- [Selling products during booking](selling-products-during-booking.md) — How to offer products in the booking flow.
- [Entry pass — client view](entry-pass-client-view.md) — How clients see and use entry passes in their profile.
- [Pay-as-you-go FAQ](../faq/pay-as-you-go-faq.md) — Common questions about entry passes and Pay-as-you-go.
