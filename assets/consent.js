/* Google tag (Google Ads, AW-18545227066) with Consent Mode v2.
   Nothing is stored and no ad cookies are set until the visitor accepts in the
   banner. The choice is kept in localStorage ("sideline-consent"); any element
   with data-consent-settings reopens the banner. Only runs on sideline.no. */
(function () {
  var ID = "AW-18545227066", KEY = "sideline-consent";
  var w = window, d = document;
  if (!/(^|\.)sideline\.no$/.test(location.hostname)) return;

  w.dataLayer = w.dataLayer || [];
  function gtag() { w.dataLayer.push(arguments); }
  w.gtag = gtag;

  function stored() { try { return localStorage.getItem(KEY); } catch (e) { return null; } }
  function grant(on) {
    var v = on ? "granted" : "denied";
    return { ad_storage: v, ad_user_data: v, ad_personalization: v, analytics_storage: v };
  }

  var choice = stored();
  var def = grant(false);
  def.wait_for_update = 500;
  gtag("consent", "default", def);
  gtag("set", "ads_data_redaction", true);
  if (choice === "granted") gtag("consent", "update", grant(true));
  gtag("js", new Date());
  gtag("config", ID);

  var s = d.createElement("script");
  s.async = true;
  s.src = "https://www.googletagmanager.com/gtag/js?id=" + ID;
  d.head.appendChild(s);

  var nb = (d.documentElement.lang || "").indexOf("en") !== 0;
  var T = nb ? {
    text: "Vi bruker informasjonskapsler fra Google Ads for å måle hvordan annonsene våre virker. Det skjer bare hvis du godtar det.",
    more: "Les mer", href: "/privacy/#nettsiden", yes: "Godta", no: "Avslå", label: "Informasjonskapsler"
  } : {
    text: "We use Google Ads cookies to measure how our ads perform, only if you accept.",
    more: "Learn more", href: "/privacy/en/#website", yes: "Accept", no: "Decline", label: "Cookies"
  };

  function save(on) {
    try { localStorage.setItem(KEY, on ? "granted" : "denied"); } catch (e) {}
    gtag("consent", "update", grant(on));
  }

  function banner() {
    if (d.getElementById("consent")) return;
    var b = d.createElement("div");
    b.id = "consent";
    b.setAttribute("role", "dialog");
    b.setAttribute("aria-label", T.label);
    b.innerHTML = '<p>' + T.text + ' <a href="' + T.href + '">' + T.more + '</a></p>' +
      '<div><button type="button" data-v="0">' + T.no + '</button>' +
      '<button type="button" data-v="1">' + T.yes + '</button></div>';
    var st = d.createElement("style");
    st.textContent =
      "#consent{position:fixed;left:16px;right:16px;bottom:calc(16px + env(safe-area-inset-bottom));z-index:1000;" +
      "max-width:640px;margin:0 auto;display:flex;flex-wrap:wrap;gap:12px 16px;align-items:center;" +
      "padding:16px;border-radius:14px;background:#141414;color:#f2f2f2;border:1px solid #2a2a2a;" +
      "box-shadow:0 8px 32px rgba(0,0,0,.5);font-size:14px;line-height:1.45}" +
      "#consent p{flex:1 1 280px;margin:0}#consent a{color:#FF6100}" +
      "#consent div{display:flex;gap:8px;margin-left:auto}" +
      "#consent button{font:inherit;font-weight:600;padding:9px 18px;border-radius:999px;cursor:pointer;" +
      "border:1px solid #444;background:transparent;color:inherit}" +
      "#consent button[data-v='1']{background:#FF6100;border-color:#FF6100;color:#000}";
    b.appendChild(st);
    b.addEventListener("click", function (e) {
      var v = e.target.getAttribute && e.target.getAttribute("data-v");
      if (v === null || v === undefined) return;
      save(v === "1");
      b.parentNode.removeChild(b);
    });
    d.body.appendChild(b);
  }

  function ready() {
    // Redirect pages move on at once; ask on the page the visitor lands on.
    if (!stored() && !d.querySelector('meta[http-equiv="refresh"]')) banner();
    d.addEventListener("click", function (e) {
      var t = e.target.closest && e.target.closest("[data-consent-settings]");
      if (t) { e.preventDefault(); banner(); }
    });
  }
  if (d.readyState === "loading") d.addEventListener("DOMContentLoaded", ready);
  else ready();
})();
