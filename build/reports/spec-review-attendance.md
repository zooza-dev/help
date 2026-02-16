# Spec Review: Attendance Quick View / Full View

**Generated:** 2026-02-16
**Feature:** Session attendance — Quick view & Full view toggle
**Status:** Released (translation keys deployed)
**Spec source:** None found — no formal spec exists for this feature

---

## Summary

The Quick view / Full view attendance toggle has been shipped but no business specification or product spec was written for it. The KB team documented the feature based on UI screenshots and codebase analysis. This report lists what we need from the dev/product team to complete the documentation.

## What we documented (based on UI + code)

- Two views: Quick view (simplified) and Full view (detailed)
- Quick view shows: 4 attendance states, "Mark all as attended" button, attended count (X/Y)
- Full view shows: everything from Quick view + make-up sessions, cancellation reasons, notes
- User can toggle between views freely
- Attended count format: "Attended 3/5"

## Questions for Dev Team

### Quick view behaviour

1. **Default view** — Is Quick view the default for all users, or does it remember the last used view per user/session?
2. **Role differences** — Do all roles (owner, instructor, receptionist, other company users) see both views? Or are some roles locked to Quick view?
3. **"Mark all as attended" scope** — Does it mark ALL clients including waiting list and make-up session clients? Or only the "Enrolled" group?
4. **"Mark all as attended" undo** — Can the user undo a bulk mark? Or do they need to manually revert individual statuses?
5. **Attended count** — What exactly do the numbers represent? Is it `attended / total_enrolled` or `attended / (enrolled + make-up)`?
6. **Make-up sessions in Quick view** — The make-up section appears below "Enrolled" in Quick view. Can make-up clients be marked in Quick view, or only in Full view?

### Full view behaviour

7. **Changes from previous version** — Did anything change in Full view with this release, or is it identical to the previous attendance UI?
8. **Session navigation** — The "Previous session" / "Next session" buttons at the top — were these added with Quick view, or did they exist before?

### Settings

9. **Company setting** — Is there a company-level setting to default all users to Quick view or Full view?
10. **Programme/class setting** — Can Quick view be disabled per programme or class (e.g. for programmes where make-up management is critical)?
11. **`trainer_attendance_management` setting** — How does the existing "limited" vs "full" attendance management setting interact with Quick view / Full view? Are they independent features?

### Mobile / responsive

12. **Mobile experience** — Does Quick view have any special mobile optimizations? (The business reason mentions fast marking on phones)
13. **Tablet/kiosk mode** — Any differences on tablet?

### Edge cases

14. **Empty session** — What does Quick view show when no clients are enrolled?
15. **Large class** — Any pagination or scrolling behaviour for classes with 30+ clients?
16. **Concurrent marking** — If two admins mark attendance simultaneously (e.g. admin + instructor), how are conflicts handled?

## Terminology issues

The codebase uses inconsistent naming:
- Translation keys use `limited_attendance_management` for role-based restriction
- UI shows "Quick view" / "Full view" for the user-facing toggle
- These appear to be **two separate features** but the relationship is unclear

**Recommendation:** Clarify in the spec whether `trainer_attendance_management = 'limited'` forces Quick view, or if they are independent axes (role-based restriction vs. UI preference).

## Missing spec

**Request:** Please create a product spec (SP-attendance-quick-view) documenting:
- Feature overview and business rationale
- Exact scope of Quick view vs Full view
- Interaction with existing `trainer_attendance_management` setting
- Role-based access matrix
- "Mark all as attended" exact behaviour and scope
- Attended count calculation logic
- Mobile-specific considerations

This will help us maintain accurate KB articles going forward.

## Affected KB articles

| Article | Action needed |
|---|---|
| `content/faq/attendance-and-catchups-faq.md` | Updated with Quick view / Full view section (done) |
| `content/faq/make-up-sessions-faq.md` | May need note about Quick view not showing make-up details |
| `content/guides/replacement-hours-complete.md` | May need note about Full view being needed for make-up management |
| `content/reference/calendar.md` | Needs mention of Quick/Full view toggle on session detail |
| `content/reference/sessions-list.md` | May need update if session list UI changed |
