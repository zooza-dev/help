import React, {useState, useEffect, useRef} from 'react';
import Layout from '@theme/Layout';
import './styles.css';

// Interactive onboarding guide. Standalone React page (outside the markdown
// pipeline) so its <details>, region switcher and localStorage never touch MDX.
// Region switcher rewrites every app + embed host live. Help links are the real
// published slugs (help.zooza.online/<area>/<slug>/).

const H = 'https://help.zooza.online';
const DOCS = 'https://docs.zooza.online/widgets';

const HOSTS = {
  eu:   {app: 'zooza.app',      api: 'https://api.zooza.app',      book: 'zooza.site/youraccountname'},
  uk:   {app: 'uk.zooza.app',   api: 'https://uk.api.zooza.app',   book: 'zooza.site/uk/youraccountname'},
  asia: {app: 'asia.zooza.app', api: 'https://asia.api.zooza.app', book: 'zooza.site/asia/youraccountname'},
};
const REGIONS = [['eu', 'Europe'], ['uk', 'UK'], ['asia', 'Asia']];

const TOC = [
  ['Is Zooza for me?', 'fit'], ['Journey', 'journey'], ['Data model', 'model'],
  ['Setup', 'setup'], ['Confirm', 'confirm'], ['Publish', 'publish'],
  ['The week', 'week'], ['Daily', 'daily'], ['More', 'more'], ['Support', 'support'],
];

const COURSE_TYPES = [
  {ico: '🎟️', tag: 'One-off event', t: 'A single date',
   d: 'One session on one day — a workshop, open day or lecture. No repeating schedule.'},
  {ico: '🔄', tag: 'Pay-as-you-go', t: 'Book & pay per session',
   d: 'Clients sign up for the activity, then pick individual sessions — drop-in yoga or pilates. Credits/passes count down.'},
  {ico: '♾️', tag: 'Membership', t: 'Recurring while classes run',
   d: <>A fixed charge on a regular cycle (e.g. monthly) for <b>as long as the class has sessions</b> — no target total, it keeps billing while the group runs.</>},
  {ico: '📅', tag: 'Term fee', t: 'One total, split into instalments', feat: true,
   d: <>You have a <b>final amount</b> to collect for a term and want to <b>split it</b> — e.g. into monthly payments across a billing period.</>},
];

const BUSINESS_MODELS = [
  ['Children — term / block', H + '/programmes/children-group-activities-block/'],
  ['Children — subscription', H + '/programmes/children-group-activities-subscription/'],
  ['Adult language school', H + '/programmes/adult-language-school/'],
  ['Individual 1-to-1', H + '/programmes/individual-lessons/'],
  ['Camps & holiday programmes', H + '/programmes/camps/'],
  ['Drop-in / pay-as-you-go', H + '/programmes/open-classes-drop-in/'],
  ['Online & hybrid', H + '/programmes/online-and-hybrid-classes/'],
  ['Franchise network', H + '/settings/franchise-network/'],
];

const JOURNEY = [
  ['🔎', 'Discover & book', 'A parent finds a class on your site and books in a few taps.'],
  ['🩰', 'Trial (optional)', 'A trial session or two to experience the class before committing.'],
  ['⭐', 'Enrolment', 'An auto invite turns the trial into a full enrolment for the term.'],
  ['💳', 'Invoice & payment', 'Invoiced automatically; paid online or by bank transfer — matched for you.'],
  ['✅', 'Attendance', 'You mark who came each session; make-up credits handle absences.'],
  ['🔁', 'Auto-enrolment', 'At term end, families roll into the next term automatically.'],
];

const SETUP = [
  {t: 'First login', path: '', help: H + '/settings/login-and-account-faq/',
   d: 'Your account arrives as an invite — log in to the app with your email and set a password.'},
  {t: 'Create your location(s)', path: '#settings/places', help: H + '/settings/creating-a-location/',
   d: 'Add every venue where classes take place. Locations are shared across all your programmes.'},
  {t: 'Set your billing period', path: '#settings/billing_periods', help: H + '/payments/billing-periods/',
   d: <>Billing periods are the term blocks used for reporting and grouping — e.g. one season. The date range is <b>optional</b>: leave it out and it simply frames the term; add it and Zooza uses the range to help you generate sessions within it.</>},
  {t: 'Add custom holidays', path: '#settings/custom_holidays', help: H + '/calendar/holiday-settings/',
   d: 'Add your own closures on top of public holidays so sessions skip them automatically.'},
  {t: 'Add trainers (optional)', path: '#settings/team', help: H + '/settings/managing-instructors/',
   d: 'Add other instructors if there will be any besides you, and set their access and pay rates.'},
  {t: 'Set up consents', path: '#settings/consents', help: H + '/settings/setting-gtc-gdpr-consents/',
   d: 'Configure the consents you collect (photo/video, health, GDPR). Consent texts use HTML tags — see the help article for formatting.'},
  {t: 'Create a programme & pricing', path: '#courses', help: H + '/payments/price-and-payment-setup/',
   d: <>Create your programme once, then set pricing. Offer parents several payment options (monthly / quarterly / yearly) — they pick at registration. Payment templates are reusable; make as many as you like.</>},
  {t: 'Create classes & sessions', path: '#courses', help: H + '/classes/creating-a-class/',
   d: 'Each class has its own capacity, trainer and venue. Sessions are generated as you build the class — skip holidays, move or edit dates; enrolled families follow automatically.'},
  {t: 'Update email templates', path: '#communication/templates', help: H + '/communication/message-templates/',
   d: 'Tailor the messages parents receive. Each opens straight in the editor:', templates: true},
  {t: 'Set up how you get paid', path: '#payments/inbound/setup?invoice_profile=0', help: H + '/payments/inbound-payments-setup/',
   d: <>Two ways — combine them if you like. <b>Payment gateway only (e.g. Stripe):</b> you're done — Zooza reads payments straight from the gateway, no bank to connect. <b>Bank transfers:</b> automate matching with the email parser (forward your bank's payment emails → matched by variable symbol) or connect <b>GoCardless</b> for direct debit.</>},
  {t: 'Connect the Zooza AI Assistant', path: '#mcp', help: H + '/mcp/claude-plugin/',
   d: 'Link Zooza to Claude or ChatGPT — it can advise you and increasingly do the work for you.'},
];

const TEMPLATES = [
  {t: 'Confirm / continue', type: 'registration_confirmation', d: '1st email after they register — verifies email & contact'},
  {t: 'Enrolment welcome', type: 'registration_done', d: 'Sent once they’ve confirmed'},
  {t: 'Session reminders', type: 'event_notification', d: 'Automatic reminder before each session'},
  {t: 'Trial booked', type: 'registration_trial_done', d: 'Trials only'},
  {t: 'After the trial', type: 'registration_trial_ended', d: 'Trials only'},
  {t: 'Follow-up nudge', type: 'registration_trial_followup', d: 'Trials only'},
  {t: 'Missed — re-engage', type: 'registration_trial_lost', d: 'Trials only'},
];

const CONFIRM = [
  ['Which pricing model — membership, term fee, pay-as-you-go or one-off?', H + '/payments/payment-templates-creation/'],
  ['Make-up / replacement classes — offered? how many, how booked?', H + '/calendar/replacement-hours-complete/'],
  ['Auto-enrolment — how families roll into the next term.', H + '/programmes/auto-enrollment/'],
  ['Payment options to offer parents (monthly / quarterly / yearly).', H + '/payments/payment-options/'],
  ['Holidays and your term dates.', H + '/calendar/holiday-settings/'],
  ['Trainers — anyone besides you?', H + '/settings/managing-instructors/'],
  ['Consents — which are required?', H + '/settings/setting-gtc-gdpr-consents/'],
];

const DAILY = [
  ['Mark attendance each session', H + '/calendar/admin-attendance-management/'],
  ['Move clients between classes', H + '/bookings/transfer-and-copy-bookings/'],
  ['Cancel or remove a client mid-term', H + '/clients/remove-client-or-user/'],
  ['Child can’t attend → add a make-up', H + '/calendar/replacement-hours-complete/'],
  ['Send payment reminders', H + '/communication/automatic-payment-reminders/'],
  ['Auto-cancel unpaid registrations', H + '/payments/auto-cancel-unpaid-registrations/'],
  ['Issue a refund', H + '/payments/stripe-refund-guide/'],
];

const MORE = [
  ['WhatsApp notifications', '#integrations/whatsapp'],
  ['Invoice profiles & invoicing', '#settings/invoice_profiles'],
  ['Google Reviews', '#feedback/reviews'],
  ['Referral & loyalty', '#payments/loyalty'],
  ['Discount campaigns', '#payments/discounts'],
  ['Team access & roles', '#settings/team'],
  ['Notifications to your inbox', '#settings/notifications'],
  ['Dashboard', '#'],
];

const WIDGETS = [
  ['📝', 'Registration', 'A form per product page', 'Each product/class page gets its own booking form, scoped to one programme, class or venue.', DOCS + '/registration-widget'],
  ['📅', 'Calendar', 'Activities view', 'A live calendar of sessions — filter by venue, course or trainer; click through to booking.', DOCS + '/calendar-widget'],
  ['📍', 'Map', 'Venue & branch map', 'Parents search by address, pick a location, see its classes and book.', DOCS + '/map-widget'],
  ['🛍️', 'Order form', 'Products & services', 'Sell videos, e-books, passes and coupons — before, during or outside a booking.', DOCS + '/checkout-widget'],
  ['🎬', 'Video', 'Members-only video', 'Secure playback for enrolled, logged-in families — your parent-zone content.', DOCS + '/video-widget'],
  ['👨‍👩‍👧', 'Parent zone', 'Client profile portal', 'History, outstanding payments, cancellations, make-ups and purchased content.', DOCS + '/profile-widget'],
];

function Guide() {
  const [region, setRegion] = useState('eu');
  const [checked, setChecked] = useState({});
  const rootRef = useRef(null);

  useEffect(() => {
    try {
      const r = localStorage.getItem('zg-region');
      if (r && HOSTS[r]) setRegion(r);
      const c = {};
      CONFIRM.forEach((_, i) => { if (localStorage.getItem('zg-chk-' + i) === '1') c[i] = true; });
      setChecked(c);
    } catch (e) { /* storage blocked — defaults are fine */ }
  }, []);

  useEffect(() => {
    if (typeof IntersectionObserver === 'undefined') return undefined;
    if (window.matchMedia && window.matchMedia('(prefers-reduced-motion: reduce)').matches) return undefined;
    const els = rootRef.current ? rootRef.current.querySelectorAll('.reveal') : [];
    const io = new IntersectionObserver((entries) => {
      entries.forEach((en) => { if (en.isIntersecting) { en.target.classList.add('in'); io.unobserve(en.target); } });
    }, {threshold: 0.08});
    els.forEach((el) => io.observe(el));
    return () => io.disconnect();
  }, []);

  const pickRegion = (r) => {
    setRegion(r);
    try { localStorage.setItem('zg-region', r); } catch (e) { /* ignore */ }
  };
  const toggle = (i) => setChecked((prev) => {
    const next = {...prev, [i]: !prev[i]};
    try { localStorage.setItem('zg-chk-' + i, next[i] ? '1' : '0'); } catch (e) { /* ignore */ }
    return next;
  });

  const host = HOSTS[region];
  const app = (path) => `https://${host.app}/${path}`;

  return (
    <div className="zog" ref={rootRef}>
      <div className="bar">
        <div className="barrow">
          <span className="rlabel">Region</span>
          <div className="seg" role="group" aria-label="Choose your Zooza region">
            {REGIONS.map(([r, label]) => (
              <button key={r} type="button" aria-pressed={region === r} onClick={() => pickRegion(r)}>{label}</button>
            ))}
          </div>
          <span className="readout mono">App: <b>{host.app}</b></span>
        </div>
        <nav className="toc" aria-label="On this page">
          {TOC.map(([label, id]) => <a key={id} href={`#${id}`}>{label}</a>)}
        </nav>
      </div>

      <div className="wrap">
        <header className="zhero" id="top">
          <span className="eyebrow">Your setup guide</span>
          <h1>Get your classes <u>live on Zooza<svg viewBox="0 0 300 12" preserveAspectRatio="none" aria-hidden="true"><path d="M2 8 C 60 2, 120 2, 160 6 S 260 10, 298 4" fill="none" stroke="#fa6900" strokeWidth="4" strokeLinecap="round"/></svg></u> — step by step.</h1>
          <p className="lead">Everything to move your programmes, payments and bookings into Zooza — with a direct link into the app and to help at every step. Set your region once and every app link points to the right place.</p>
          <div className="readout-box">
            <span className="pill">✔ Region set</span>
            <span>App: <b className="mono">{host.app}</b></span>
            <span>Embed API: <b className="mono">{host.api.replace('https://', '')}</b></span>
          </div>
        </header>

        {/* FIT */}
        <section id="fit" className="reveal">
          <div className="sec-head">
            <span className="eyebrow">Start here</span>
            <h2>Does my business fit Zooza?</h2>
            <p>Almost every class-based business does. First find the pricing shape that matches how you actually collect money — this decides most of your setup.</p>
          </div>
          <div className="grid g2">
            {COURSE_TYPES.map((c) => (
              <div key={c.tag} className={'card ctype' + (c.feat ? ' feat' : '')}>
                <span className="ico">{c.ico}</span><span className="tag">{c.tag}</span>
                <h3>{c.t}</h3><p>{c.d}</p>
              </div>
            ))}
          </div>
          <div className="callout">
            <p><span className="k">Membership vs. term fee — don’t mix them up.</span> A <b>membership</b> keeps billing a recurring amount for as long as the class has sessions — there’s no target total. <b>Term fee</b> is one known total for a term, split into instalments that stop when the term ends. Most schools splitting a course price monthly want <b>term fee</b>. <a href={H + '/payments/payment-templates-creation/'} target="_blank" rel="noopener">See payment templates →</a></p>
          </div>
          <p className="note">Parents see the payment options you allow (monthly / quarterly / yearly) at registration, choose one, and Zooza handles the rest.</p>

          <div className="sec-head" style={{marginTop: '36px', marginBottom: '16px'}}>
            <span className="eyebrow">Find your setup</span>
            <h3 style={{fontSize: '21px', color: 'var(--heading)'}}>Guides for your kind of business</h3>
            <p>Start from a worked example that matches you — each is a full setup walkthrough on help.</p>
          </div>
          <div className="grid g3">
            {BUSINESS_MODELS.map(([label, url]) => (
              <a key={label} className="card bm" href={url} target="_blank" rel="noopener"><h3>{label}</h3><span className="tag">open guide →</span></a>
            ))}
            <a className="card bm feat" href={H + '/programmes/business-models/'} target="_blank" rel="noopener"><h3>Not sure? Find your setup</h3><span className="tag">decision guide →</span></a>
          </div>
        </section>

        {/* JOURNEY */}
        <section id="journey" className="reveal">
          <div className="sec-head">
            <span className="eyebrow">The big picture</span>
            <h2>The parent journey</h2>
            <p>The whole lifecycle, end to end — this is what every setting below is in service of.</p>
          </div>
          <ol className="timeline">
            {JOURNEY.map(([emoji, t, d], i) => (
              <li key={t}><span className="dot">{emoji}</span><h3><span className="n">{i + 1}</span> {t}</h3><p>{d}</p></li>
            ))}
          </ol>
          <div className="tip" style={{marginTop: '8px'}}><span className="k">Tip — always test as a parent.</span> Book a trial on your own offer and walk the full journey. It’s the fastest way to be sure everything works before the questions come in.</div>
        </section>

        {/* DATA MODEL */}
        <section id="model" className="reveal">
          <div className="sec-head">
            <span className="eyebrow">How Zooza is organised</span>
            <h2>The data model</h2>
            <p>Three layers for what you offer, plus how people and orders sit against them. <a href={H + '/programmes/programme-class-session-definition/'} target="_blank" rel="noopener">Full explanation →</a></p>
          </div>
          <div className="chain">
            <div className="node p"><div className="ico">📚</div><div className="nm">Programme</div><small>Your overall offering.<br/>Set up once.</small></div>
            <div className="arrow">›</div>
            <div className="node c"><div className="ico">👯</div><div className="nm">Class</div><small>A group people book into.<br/>Capacity · trainer · place. Added often.</small></div>
            <div className="arrow">›</div>
            <div className="node"><div className="ico">📅</div><div className="nm">Session</div><small>A concrete date &amp; time.<br/>Movable · skippable · deletable.</small></div>
          </div>
          <p className="note" style={{textAlign: 'center'}}>Editing sessions (skip a holiday, move a date) never drops the enrolled families — everyone in the class comes along.</p>
          <div className="grid g2" style={{marginTop: '20px'}}>
            <div className="panel"><h3>👤 Client → Booking</h3><p>A <b>client</b> is the person you hold consents for (usually a parent linked to a child). A <b>booking</b> is their registration into a class. One client → many bookings.</p></div>
            <div className="panel"><h3>🛍️ Orders (products)</h3><p>Bookings are for <b>services</b> (classes). <b>Orders</b> are for <b>products</b> — merch, entry passes, digital content and videos — a separate flow from a class booking.</p></div>
          </div>
        </section>

        {/* SETUP */}
        <section id="setup" className="reveal">
          <div className="sec-head">
            <span className="eyebrow">Do these in order</span>
            <h2>Setup — step by step</h2>
            <p>Open each step. Every one links straight into Zooza (region-aware) and to its help article.</p>
          </div>
          <div className="acc">
            {SETUP.map((s, i) => (
              <details key={s.t} className="step">
                <summary>
                  <span className="idx">{i + 1}</span>
                  <span className="st">{s.t}</span>
                  {s.path ? <span className="path mono">{s.path}</span> : null}
                  <span className="caret">›</span>
                </summary>
                <div className="body">
                  <p>{s.d}</p>
                  {s.templates ? (
                    <>
                      <div className="tgrid">
                        {TEMPLATES.map((t) => (
                          <a key={t.type} href={app(`#communication/templates?type=${t.type}`)} target="_blank" rel="noopener">
                            <b>{t.t}</b><em>{t.d}</em><span>open in editor →</span>
                          </a>
                        ))}
                      </div>
                      <p className="note">Order for an ongoing programme: <b>Confirm</b> (they verify email &amp; contact) → <b>Enrolment welcome</b>. Trial emails send only if trials are switched on. These are the <b>ongoing-class</b> templates — <b>one-off events</b> and <b>pay-as-you-go</b> have their own sets.</p>
                    </>
                  ) : null}
                  <div className="links">
                    <a href={app(s.path)} target="_blank" rel="noopener">open in Zooza →</a>
                    <a className="help" href={s.help} target="_blank" rel="noopener">help →</a>
                  </div>
                </div>
              </details>
            ))}
          </div>
        </section>

        {/* CONFIRM */}
        <section id="confirm" className="reveal">
          <div className="sec-head">
            <span className="eyebrow">Decisions that shape the offer</span>
            <h2>Confirm before you build</h2>
            <p>Tick these off — they decide how the whole offer behaves. Your progress is saved on this device.</p>
          </div>
          <ul className="check">
            {CONFIRM.map(([task, help], i) => (
              <li key={i}>
                <button type="button" aria-pressed={!!checked[i]} aria-label="Toggle done" onClick={() => toggle(i)}>{checked[i] ? '✓' : ''}</button>
                <span className={'lbl' + (checked[i] ? ' done' : '')}>{task}</span>
                <a href={help} target="_blank" rel="noopener">help →</a>
              </li>
            ))}
          </ul>
        </section>

        {/* PUBLISH */}
        <section id="publish" className="reveal">
          <div className="sec-head">
            <span className="eyebrow">Go live</span>
            <h2>Publish — how your offer reaches clients</h2>
            <p>Setup done. Now put it in front of parents. Embed exactly the piece you need on your own website — one widget per page — or let Zooza host the whole thing. You configure every widget in one place.</p>
          </div>
          <div className="cta-row">
            <a className="btn" href={app('#widgets')} target="_blank" rel="noopener" style={{color: '#fff'}}>Configure widgets in Zooza →</a>
            <a href={DOCS + '/'} target="_blank" rel="noopener">Developer docs →</a>
          </div>
          <div className="grid g3">
            {WIDGETS.map(([ico, tag, t, d, url]) => (
              <a key={tag} className="card wcard" href={url} target="_blank" rel="noopener">
                <span className="ico">{ico}</span><span className="tag">{tag}</span>
                <h3>{t}</h3><p>{d}</p><span className="tag" style={{marginTop: 'auto'}}>docs →</span>
              </a>
            ))}
          </div>
          <div className="split" style={{marginTop: '16px'}}>
            <div className="panel">
              <h3>No website? Zooza hosts it</h3>
              <p>Share the ready booking page for any programme — or, with no site at all, get a full hosted mini-site at <b className="mono">{host.book}</b>. Set it all up under <b>Widgets</b>.</p>
              <div className="links"><a href={app('#widgets')} target="_blank" rel="noopener">open widgets settings →</a></div>
            </div>
            <div className="panel">
              <h3>Region-aware embed</h3>
              <p style={{marginBottom: '10px'}}>Your embed points at the API host for your region — set automatically:</p>
              <div className="snippet mono"><span className="t">&lt;script</span> <span className="a">data-widget-id</span>=<span className="v">"zooza"</span> <span className="a">data-zooza-api-url</span>=<span className="v">"{host.api}"</span><span className="t">&gt;&lt;/script&gt;</span></div>
            </div>
          </div>
          <p className="note">Full styling is website-side (your CSS); scoping and options are set per programme in the app.</p>
        </section>

        {/* WEEK */}
        <section id="week" className="reveal">
          <div className="sec-head">
            <span className="eyebrow">Running it</span>
            <h2>Managing the week</h2>
          </div>
          <div className="panel">
            <p>The <b>Calendar</b> runs your <b>current week</b> — attendance, cancellations, day-to-day. But <b>changes to a class</b> (dates, times, trainer, venue) are made in the <b>class schedules list</b>, not the calendar.</p>
            <div className="links">
              <a href={app('#calendar')} target="_blank" rel="noopener">open calendar →</a>
              <a href={app('#courses/schedules')} target="_blank" rel="noopener">open class schedules →</a>
              <a className="help" href={H + '/calendar/calendar/'} target="_blank" rel="noopener">help →</a>
            </div>
          </div>
        </section>

        {/* DAILY */}
        <section id="daily" className="reveal">
          <div className="sec-head">
            <span className="eyebrow">Everyday tasks</span>
            <h2>Daily business</h2>
          </div>
          <div className="rows">
            {DAILY.map(([task, help]) => (
              <div className="zrow" key={task}><span className="dot2">•</span><span className="b">{task}</span><a href={help} target="_blank" rel="noopener">help →</a></div>
            ))}
          </div>
        </section>

        {/* MORE */}
        <section id="more" className="reveal">
          <div className="sec-head">
            <span className="eyebrow">When you’re ready</span>
            <h2>Integrations &amp; later</h2>
            <p>Layer these on once the basics run. Each opens in Zooza.</p>
          </div>
          <div className="grid g2">
            {MORE.map(([label, path]) => (
              <a key={label} className="card" href={app(path)} target="_blank" rel="noopener" style={{display: 'block'}}>
                <h3 style={{color: 'var(--ink-deep)'}}>{label}</h3><span className="tag">open in Zooza →</span>
              </a>
            ))}
          </div>
        </section>

        {/* SUPPORT */}
        <section id="support" className="reveal">
          <div className="support">
            <span className="eyebrow">We’re here for you</span>
            <h2 style={{marginTop: '8px'}}>Bring the problem, not the button</h2>
            <p style={{margin: '12px 0 0', color: 'var(--ink)'}}>We watch the in-app chat and reply fast — or book a call whenever you need one. Best way to work with us: describe what you’re trying to solve → ask the Zooza AI Assistant or ChatGPT → if it’s still not solved, send it over. There may already be an answer, or we’ll build one. ✨</p>
            <a className="btn" style={{marginTop: '18px'}} href="https://meetings-eu1.hubspot.com/zooza" target="_blank" rel="noopener">Book a meeting →</a>
          </div>
        </section>
      </div>
    </div>
  );
}

export default function OnboardingGuidePage() {
  return (
    <Layout title="Setup guide" description="Everything to get your classes live on Zooza — step by step, region-aware, with links into the app and to help.">
      <Guide/>
    </Layout>
  );
}
