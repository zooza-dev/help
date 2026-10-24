# Thinksmart → Zooza: Migration Reference
## babyballet Dubai — Kate

**Purpose:** For each key workflow, this document shows how things work in Thinksmart vs how they work in Zooza — so you know what to expect and what will feel different.

**Note:** The Thinksmart column is based on what we observed during your onboarding and from your UK babyballet account. Please flag anything that doesn't match. The Zooza column reflects how the system currently works.

---

## 1. Creating locations (venues)

| | Thinksmart | Zooza |
|---|---|---|
| **Where** | Settings | Settings → Team & Settings → Locations → Add location |
| **What you add** | Name, address | Name, address, optional map link |
| **Map link in emails** | Map links sent manually in emails | Same — map links must be added manually in email templates. The system doesn't auto-pull from the location record. |

**What changes:** Essentially the same. The gap is that neither system auto-includes map links in emails — you add them once into the email template and they stay.

---

## 2. Creating instructors and giving them access

| | Thinksmart | Zooza |
|---|---|---|
| **Adding an instructor** | Settings | Settings → Team & Settings → Instructors → Invite by email |
| **What instructors see** | Instructors have a restricted view (registers/attendance only) | ⚠️ Instructors currently see the full admin interface — same view as you. A dedicated limited view is planned but not yet released. |
| **Invite delivery** | Works reliably | Invite emails occasionally land in spam. If instructor doesn't receive it — check spam first, then re-send from settings. |

**What changes:** The instructor experience is the main difference. In Thinksmart your teachers see only what they need. In Zooza right now they see everything — which is overwhelming. Brief Claire and your other teachers on what to focus on: Calendar → today's class → attendance. Ignore everything else for now.

---

## 3. Creating billing periods (terms)

| | Thinksmart | Zooza |
|---|---|---|
| **Concept** | Dedicated "billing period" entity, shown with actual term dates (e.g. "Autumn Term Sep–Oct 2025") | No separate billing period entity. Each programme has a start and end date. Zooza currently labels billing periods by academic year (e.g. "2025/2026") rather than term dates. |
| **Where you set it** | Billing period settings, then assign classes to it | Set directly on the programme: start date, end date, number of sessions |

**What changes:** You mentioned this feels less clear in Zooza — billing periods show "2025/2026" rather than "Autumn Term: 5 Sep – 25 Oct 2025". This is a known UX gap. Workaround: name your programmes to include the term dates (e.g. "babyballet Tinies — Autumn 2026").

---

## 4. Creating courses / programme types

| | Thinksmart | Zooza |
|---|---|---|
| **What it's called** | Course | Programme |
| **Private links / separate databases** | In Thinksmart you could create different databases and multiple booking links for different things (e.g. annual show, nursery partnerships, regular classes — each with its own separate database) | One account, one database. Multiple programmes each have their own booking link. Private/secret booking links (not publicly listed) are on the roadmap but not yet available. |
| **Where to create** | Courses section | Programmes → New programme |

**What changes:** The main difference is multiple databases. In Thinksmart you could completely separate, say, a nursery session from your regular timetable. In Zooza everything is in one account, but you can use separate programmes with separate links and control which ones are publicly visible. For truly private links (e.g. an Italia Conti-only booking page) — we have a workaround using direct links, but the feature isn't fully built yet.

---

## 5. Creating group classes with sessions (timetable)

| | Thinksmart | Zooza |
|---|---|---|
| **Edit once → applies everywhere** | Yes — change the class time or instructor once, it updates everywhere | ⚠️ No. Zooza has three separate layers: Programme → Class → Session. Changing a Session does not update the Class, and vice versa. |
| **Changing instructor or time** | One change updates all upcoming sessions | You must explicitly choose: "this session only" or "all upcoming sessions in this class" |
| **Creating a class** | Create within a course | Must have a Programme first → then add a Class inside it → Sessions auto-generate from the class schedule |

**What changes:** This is the biggest mental model shift from Thinksmart. In Zooza, editing one session doesn't cascade upward. Always make structural changes (instructor, time, price) at the **Class** level if you want them to apply going forward — not at the individual Session level.

⚠️ Always create in this order: Programme first → Class inside it → Sessions are auto-generated. Creating a Class requires a Programme to exist first.

---

## 6. Setting payment rules

| | Thinksmart | Zooza |
|---|---|---|
| **Payment gateway** | ClearAccept (after the Thinksmart/ClearAccept merger) — 1.4% + 20p per transaction | Stripe for card payments — fees depend on your Stripe plan. GoCardless for direct debit — 1% + 20p + VAT. |
| **Direct debit (GoCardless)** | Already using GoCardless for all babyballet UK invoices — clients set up a DD mandate, payments collected 5 working days after mandate signed | Same GoCardless integration. Setup is the same: client gets a link to sign the mandate, payment collects on the due date. |
| **When payments collect** | All invoices go out on the same day, all payments collected on the same day — cashflow predictability | ⚠️ Zooza collects each payment on its individual due date (e.g. registration date + X days). This means payments come in on different days. It *can* be configured to batch on the same date — we'll set this up for you. |
| **Payment model** | Termly invoicing + GoCardless for collection | Set at programme level: term / drop-in / single event. GoCardless or Stripe per booking. |

**What changes:** The payment gateway switches from ClearAccept to Stripe + GoCardless (GoCardless stays the same — you already know it). The key operational change is the payment collection timing — we'll configure Zooza to match your cashflow preference (all on one date).

---

## 7. Client booking and payment plan (automated)

| | Thinksmart babyballet process | Zooza process |
|---|---|---|
| **After 2nd trial class** | Automated email sent with invoice + GoCardless mandate link. Once GoCardless notification arrives → admin manually enrols client for remainder of term. | After instructor marks trial as Attended → Zooza automatically sends parent a self-registration link. Parent completes registration and payment themselves. Admin does not need to enrol manually. |
| **GoCardless activation** | Client clicks link → sets up mandate → admin gets notification → admin action required | Client clicks link in the auto-enrolment email → sets up mandate or pays by card → Zooza handles the rest automatically |
| **Term renewal (subsequent terms)** | "You will automatically be reserved a place in each term and an invoice will be sent just before the end of the current term" | Auto-enrolment: Zooza sends clients a link to confirm + pay for the new term. Clients must take action — it's not fully silent auto-renewal. |

**What changes:** In Thinksmart, you control the enrolment step — you manually confirm each client after the GoCardless notification. In Zooza, this is handled by the client themselves via the self-registration link. Less admin work, but requires trust in the automation. We'll walk you through the first term cycle together.

---

## 8. Transferring a client to a different class

| | Thinksmart | Zooza |
|---|---|---|
| **How** | [Confirm: is this in the client record or the booking?] | Bookings → find the booking → Transfer → select destination class |
| **Payment balance** | [Confirm: does payment carry over automatically?] | You choose at the time of transfer: carry over payment balance or not |
| **Client notification** | [Confirm: does client get notified?] | Client receives automatic notification of the class change |

**What changes:** Transfer works well in Zooza. The entry point isn't obvious (it's on the booking detail, not the client profile) — we'll show you where to find it.

---

## 9. Cancelling a registration

| | Thinksmart | Zooza |
|---|---|---|
| **How** | Admin manually removes client from enrolment on the system — spot then opens up on the website automatically | Bookings → find booking → Cancel registration |
| **What happens to the spot** | Opens immediately on the website | Same — spot becomes available again for new bookings |
| **Waiting list** | Admin contacts waiting list client manually to offer the space | Same — admin notifies waiting list manually (see section 19) |

**What changes:** Functionally the same. The menu location is different — you need to find the booking first, then cancel from within it.

---

## 10. Refunding a payment

| | Thinksmart | Zooza |
|---|---|---|
| **Where** | Refunds processed within Thinksmart directly | ⚠️ Zooza does **not** have a native refund button. Card refunds are issued directly in Stripe. GoCardless refunds are issued via GoCardless dashboard. Then manually marked in Zooza. |
| **Process for card refunds** | Within the system | Log in to Stripe → find the payment → Issue refund. Then in Zooza: open the booking → record the adjustment. |
| **Bulk refunds** | [Confirm: can you bulk refund in Thinksmart?] | Not possible in Zooza — each refund must be done individually in Stripe. |
| **GoCardless refunds** | Via GoCardless integration | Via GoCardless dashboard directly |

**What changes:** This is the biggest operational difference. You're used to refunding inside the software. In Zooza you go to Stripe or GoCardless first, then update Zooza. Agree your refund policy before go-live — handling many refunds reactively is the hardest scenario.

⚠️ **Stripe balance note:** If your Stripe balance is zero or negative, card refunds may be delayed. Ensure your Stripe account has funds before processing refunds, or upgrade to a standard Stripe account.

---

## 11. Invoicing (automated)

| | Thinksmart babyballet | Zooza |
|---|---|---|
| **How invoices are generated** | Invoice sent manually (or semi-automatically) by admin at end of term for next term. Invoice attached to email as PDF. | Auto-generated every time a payment is recorded or a booking is created. Available as PDF in the booking detail and Reports. |
| **Invoice sent to client** | Attached to the term renewal email | Clients can download from their Parent Portal. Admin can also download and send manually. |
| **Payment collection date** | All clients pay on the same day (cashflow preference) | Configurable — we'll match your preferred collection date. |
| **Accountant export** | [Confirm: CSV? XML? What format?] | Reports & Insights → filter by date range → export (CSV, XML, PDF). Compatible with Xero. |
| **Reporting trust** | Known issue: babyballet franchisees don't fully trust Thinksmart's reporting figures — some admins manually re-count | Zooza reporting is real-time. Worth cross-checking against your own records for the first term to build confidence. |

**What changes:** Invoicing in Zooza is more automated — invoices generate without you doing anything. The difference is visibility: in Thinksmart you created the invoice and knew exactly when it went out. In Zooza it happens automatically, so you need to know where to find it.

---

## 12. Creating new terms

| | Thinksmart | Zooza |
|---|---|---|
| **Opening bookings for a new term** | You can open bookings for a new term at any time — even half a term in advance (parents enquire early) | You can do the same: either add future sessions to an existing ongoing class, or copy the programme and set future dates. Sessions remain bookable as soon as they're created. |
| **Term setup effort** | [Confirm: one click / wizard, or manual class setup?] | Currently multi-step: copy programme → adjust dates → run auto-enrolment. There's no one-button term wizard yet. We'll do the first one together. |
| **Client re-enrolment** | "You will automatically be reserved a place in each term and an invoice will be sent just before the end of the current term" | Zooza sends clients a link to confirm and pay. They must take action — it's not silent auto-renewal. Clients who don't respond need to be chased manually. |

**What changes:** You can open bookings for next term early — same as Thinksmart. The renewal email is similar in spirit but the client has to click through and pay rather than just having their GoCardless mandate charged silently. Expect a small number of clients who need a nudge each term.

---

## 13. Trials: collection and automation (including payments)

**babyballet UK Thinksmart process (what you told us):**
1. Client books 3-week trial online
2. After 2nd trial class → automated email sent with invoice for rest of term + £14 joining fee + GoCardless mandate link
3. Admin receives GoCardless notification → admin manually enrols client for remainder of term
4. Payment collected 5 working days after mandate signed
5. Client reserved automatically each subsequent term, invoice sent before term end

**Zooza process:**

| Step | Thinksmart | Zooza |
|------|-----------|-------|
| Client books trial | Online via booking page | Online via booking page — admin cannot create a trial manually ⚠️ |
| After trial completion | Admin triggers enrolment after GoCardless notification | System auto-sends enrolment link to parent after instructor marks "Attended" |
| Client enrolment | Admin manually enrols the client | Client self-registers via the link — no admin action needed |
| Payment | GoCardless, collected 5 days after mandate signed | GoCardless or Stripe — timing set at programme level |
| Trial missed | [Confirm: how do you handle "trial lost" in TS?] | Status becomes "Trial lost". Rescheduling requires a multi-step workaround — no dedicated button yet. |

**What changes:** The biggest shift is who does the enrolment step. In Thinksmart you enrol the client manually after the GoCardless ping. In Zooza, the client does it themselves via an automated link. This is less work for you, but requires trusting the automation — and requires clients who are comfortable with self-service.

⚠️ **Known gap:** Admin cannot create a trial manually in Zooza. If a parent walks in or calls, you'll need to send them to the booking page. We have a workaround process for this.

---

## 14. Moving trial dates (if client can't attend)

| | Thinksmart | Zooza |
|---|---|---|
| **How** | [Confirm: is there a simple reschedule button?] | No dedicated "reschedule trial" button. Workaround: mark the session as "Did not attend" → trial stays in progress → manually book the client into a session in a different class using the make-up flow, then set it as their trial session. |
| **Who does it** | Admin | Admin |

**What changes:** This is a workaround, not a clean flow. It's manageable (3–4 steps once you know them) but not intuitive. We'll write the exact steps for you and keep them in the shared document.

---

## 15. Upsell (selling additional products with a registration)

| | Thinksmart | Zooza |
|---|---|---|
| **Uniform / merchandise** | Sold via the babyballet website shop separately — not integrated into the booking system | Can be set up under Orders & Products in Zooza. Can be offered during the booking flow or as standalone orders. |
| **Welcome pack / joining fee** | £14 joining fee charged at enrolment, then physical welcome pack handed over by teacher | Same structure: one-off registration fee at enrolment. Physical welcome pack is separate — not managed in Zooza. |
| **Annual show / events** | Separate database in Thinksmart | Separate programme in Zooza with its own booking link |

**What changes:** Upsell items (merchandise, extras) can be added in Zooza under Products & Services, but it's not a full e-commerce catalogue. Good for simple items (e.g. extra class, summer camp, show ticket). For the full uniform range — the existing babyballet shop handles that better.

---

## 16. Attendance (instructor view)

| | Thinksmart | Zooza |
|---|---|---|
| **How instructors mark attendance** | [Confirm: dedicated instructor app, paper register, or web login?] | Calendar → click today's session → mark each client: Attended / Did not attend / Cancelled |
| **Device** | [Confirm: phone app, tablet, desktop?] | Web browser on any device. Works on phone — but requires scrolling through the full client list, which is slow for large classes. |
| **Speed** | [Confirm: quick tick list or form-based?] | Current interface is functional but not optimised for phone use during class. Better to mark attendance on desktop after class, or have Claire log in before class on her phone and pre-load the register. |
| **Print registers** | You wanted to print registers for Claire (from your chat) | Not a built-in print view — but you can export the session list. Alternatively, Claire can log in on her phone during class. |

**What changes:** If your teachers currently use a fast dedicated app or simple list, they'll notice the difference in Zooza. It's workable but slower. A faster instructor view is on the roadmap.

---

## 17. Logging into the system

| | Thinksmart | Zooza |
|---|---|---|
| **Admin login** | Email + password | Email + password |
| **Instructor login** | Restricted view — teachers see only registers and attendance | ⚠️ Same login as admin, same interface. No restricted instructor mode yet. |
| **Franchise overview** | [Confirm: does babyballet HQ have an overview across all franchisees?] | Yes — Zooza supports a network account where the franchisor can view all franchise accounts |

**What changes:** Instructor access is the main change. Brief your teachers on what to ignore. Claire (and any future instructors) will see the full admin interface until the restricted instructor view is built.

---

## 18. Sending emails (and WhatsApp)

| | Thinksmart | Zooza |
|---|---|---|
| **Automated emails** | Sends automated emails (trial confirmation, invoice after 2nd trial, term renewal reminders) | Same — Zooza sends: booking confirmation, trial confirmation, payment receipt, payment reminder, auto-enrolment link, make-up notification |
| **Email templates** | Configured per course/event | Configured per course — customisable templates for each trigger |
| **Bulk email to a class** | [Confirm: how do you email all clients in a class?] | Classes → select class → Send email. Or: Bookings → filter by class → select all → Send email. |
| **WhatsApp integration** | Not in Thinksmart | Available in Zooza (requires Meta Business account setup — already in progress for your account) |
| **Sender address** | [Confirm: your own domain or Thinksmart domain?] | Zooza sends from a Zooza domain by default. Custom domain sending is available for VIP/high-volume accounts. |
| **Email history** | [Confirm: can you see sent emails?] | Yes — logged, but not prominent. You have to look for it. |

**What changes:** Email automation is similar — the triggers and structure are the same. WhatsApp is an addition (not in Thinksmart). Main difference to review: check the default Zooza templates before go-live and adjust them to match the babyballet tone. The trial email sequence is particularly important to get right.

---

## 19. Waiting list process

| | Thinksmart | Zooza |
|---|---|---|
| **When class is full** | "Book Now" button automatically changes to "Waiting List" button on the booking page | When class is full: client sees "Class full". They can click to join the waiting list. Admin receives a notification. |
| **Client action** | Client self-joins waiting list | Client self-adds to waiting list |
| **Admin action** | Admin contacts waiting list client manually when a space opens | Admin gets notification → manually offers space to next waiting list client |
| **Automated space offer** | [Confirm: does TS auto-notify waiting list when space opens?] | Admin must manually notify — it's not automatic when a cancellation frees a spot |

**What changes:** The client-facing experience is similar — "Book Now" vs "Join Waiting List". The admin side is manual in both systems. The one extra thing to know in Zooza: trial bookings count toward class capacity (this surprised you early on). If a class shows as "full" but you have trials in it, that's why.

---

## 20. Make-up sessions (replacement classes)

| | Thinksmart | Zooza |
|---|---|---|
| **Your policy** | "Missed sessions within the block are non-refundable" (from your email templates) | Same policy is possible — make-up sessions are optional. If you offer them, they're configured per programme. |
| **How make-ups work** | [Confirm: do you currently offer make-up sessions?] | Admin cancels a session → optionally enables make-up availability → clients receive notification and can self-book a replacement slot via their Parent Portal |
| **Tracking** | [Confirm: do you track make-up usage?] | Make-up sessions report in Zooza. Currently no location filter — known gap. |

**What changes:** If you don't currently offer make-up sessions (your email templates say "missed sessions are non-refundable"), this is optional in Zooza too. You'd only need to configure it if you decide to offer them.

---

## 21. Capacity management on sessions

| | Thinksmart | Zooza |
|---|---|---|
| **Setting capacity** | Set per class | Set per class (applies to all sessions) |
| **What happens when full** | "Book Now" automatically becomes "Waiting List" | Class shows as full. Existing enrolled clients completing payment also see "Class full" — ⚠️ known issue |
| **Trials counting toward capacity** | [Confirm: do trials take up a class spot in TS?] | ⚠️ Yes — trial bookings count toward class capacity in Zooza. If you have 10 enrolled + 2 trials in a class of 12, the class shows as full — even to enrolled clients completing payment. Workaround: set capacity slightly higher than your target and monitor manually. |
| **Admin capacity override** | [Confirm: can you override capacity in TS?] | Yes — admin can manually add clients above capacity if needed |

**What changes:** The trial-counts-toward-capacity behaviour is the key surprise. We recommend setting your class capacity 2–3 spots higher than your target to leave room for active trials. We'll monitor this together in your first term.

---

## Summary: biggest changes to expect

| Area | Thinksmart | Zooza | Impact |
|------|-----------|-------|--------|
| Programme/class structure | Edit once → applies everywhere | 3-layer hierarchy (Programme → Class → Session) | **High** — needs practice |
| Instructor access | Restricted view (registers only) | Full admin interface | **High** — brief your teachers |
| Client enrolment after trial | Admin manually enrols after GoCardless ping | Client self-enrols via automated link | **Medium** — less admin work but different trust model |
| Payment collection timing | All on same day | Individual due dates (can be configured to same day) | **Medium** — we'll set this up for you |
| Refunds | Within Thinksmart | Via Stripe or GoCardless dashboard, then marked in Zooza | **High** — workflow change |
| Term rebooking | [Confirm: one-button?] | Multi-step (copy → adjust → auto-enrolment) | **Medium** — first one done together |
| Waiting list | "Book Now" → "Waiting List" automatically | Same client experience, admin action still manual | **Low** |
| Trial capacity | [Confirm: do trials count toward capacity?] | Trials count toward capacity — adjust your capacity settings | **Medium** |
| Billing period display | Actual term dates shown | Academic year shown (e.g. "2025/2026") | **Low** — naming workaround |
| Reporting | Not fully trusted by UK franchisees | Real-time, cross-check first term for confidence | **Low** |
| WhatsApp | Not available | Available (in setup) | **Positive** |
| Payment gateway | ClearAccept | Stripe + GoCardless (GoCardless same as before) | **Medium** — new Stripe setup |

---

*Prepared: May 2026*
*Based on: babyballet Dubai onboarding conversations (Aug 2025–May 2026) + babyballet UK Thinksmart email templates and process descriptions*
*Items marked [Confirm] are where we want Kate to verify or complete*
