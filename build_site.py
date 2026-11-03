#!/usr/bin/env python3
"""Write the static Notchy site. The pages are plain HTML; this only fills them."""

import html
import pathlib
from datetime import datetime

ROOT = pathlib.Path(__file__).resolve().parent
Q = (
    "What is Notchy for Mac? It turns the notch at the top of the screen into something you can use. "
    "A soft glow appears as the pointer gets near and gets brighter the closer it gets. "
    "It pulses amber when something needs approval and green when it is done. "
    "Rest the pointer on the notch, or click it, and a panel drops down with app shortcuts "
    "(Finder, Safari and Terminal by default), screenshots of the whole screen, an area, or a scrolling page, "
    "and screen recording of the whole screen or an area, with a timer and Stop. "
    "Tools include a focus timer, drop shelf, copy text from the screen, Scan QR, a color picker, keep awake, "
    "a world clock, and optional camera mirror, Downloads alerts and next meeting. "
    "Keyboard shortcuts Control Option Command 3, 4 and 7 take screenshots. "
    "Control Option Command 5 and 6 start and stop recordings. "
    "In a full-screen app the glow stays off and only a click opens the panel. "
    "Notchy is a Mac app from Jabble."
)
ASK = [
    ("ChatGPT", "https://chatgpt.com/?q=", "M9.205 8.658v-2.26c0-.19.072-.333.238-.428l4.543-2.616c.619-.357 1.356-.523 2.117-.523 2.854 0 4.662 2.212 4.662 4.566 0 .167 0 .357-.024.547l-4.71-2.759a.797.797 0 00-.856 0l-5.97 3.473zm10.609 8.8V12.06c0-.333-.143-.57-.429-.737l-5.97-3.473 1.95-1.118a.433.433 0 01.476 0l4.543 2.617c1.309.76 2.189 2.378 2.189 3.948 0 1.808-1.07 3.473-2.76 4.163zM7.802 12.703l-1.95-1.142c-.167-.095-.239-.238-.239-.428V5.899c0-2.545 1.95-4.472 4.591-4.472 1 0 1.927.333 2.712.928L8.23 5.067c-.285.166-.428.404-.428.737v6.898zM12 15.128l-2.795-1.57v-3.33L12 8.658l2.795 1.57v3.33L12 15.128zm1.796 7.23c-1 0-1.927-.332-2.712-.927l4.686-2.712c.285-.166.428-.404.428-.737v-6.898l1.974 1.142c.167.095.238.238.238.428v5.233c0 2.545-1.974 4.472-4.614 4.472zm-5.637-5.303l-4.544-2.617c-1.308-.761-2.188-2.378-2.188-3.948A4.482 4.482 0 014.21 6.327v5.423c0 .333.143.571.428.738l5.947 3.449-1.95 1.118a.432.432 0 01-.476 0zm-.262 3.9c-2.688 0-4.662-2.021-4.662-4.519 0-.19.024-.38.047-.57l4.686 2.71c.286.167.571.167.856 0l5.97-3.448v2.26c0 .19-.07.333-.237.428l-4.543 2.616c-.619.357-1.356.523-2.117.523zm5.899 2.83a5.947 5.947 0 005.827-4.756C22.287 18.339 24 15.84 24 13.296c0-1.665-.713-3.282-1.998-4.448.119-.5.19-.999.19-1.498 0-3.401-2.759-5.947-5.946-5.947-.642 0-1.26.095-1.88.31A5.962 5.962 0 0010.205 0a5.947 5.947 0 00-5.827 4.757C1.713 5.447 0 7.945 0 10.49c0 1.666.713 3.283 1.998 4.448-.119.5-.19 1-.19 1.499 0 3.401 2.759 5.946 5.946 5.946.642 0 1.26-.095 1.88-.309a5.96 5.96 0 004.162 1.713z"),
    ("Claude", "https://claude.ai/new?q=", "M4.709 15.955l4.72-2.647.08-.23-.08-.128H9.2l-.79-.048-2.698-.073-2.339-.097-2.266-.122-.571-.121L0 11.784l.055-.352.48-.321.686.06 1.52.103 2.278.158 1.652.097 2.449.255h.389l.055-.157-.134-.098-.103-.097-2.358-1.596-2.552-1.688-1.336-.972-.724-.491-.364-.462-.158-1.008.656-.722.881.06.225.061.893.686 1.908 1.476 2.491 1.833.365.304.145-.103.019-.073-.164-.274-1.355-2.446-1.446-2.49-.644-1.032-.17-.619a2.97 2.97 0 01-.104-.729L6.283.134 6.696 0l.996.134.42.364.62 1.414 1.002 2.229 1.555 3.03.456.898.243.832.091.255h.158V9.01l.128-1.706.237-2.095.23-2.695.08-.76.376-.91.747-.492.584.28.48.685-.067.444-.286 1.851-.559 2.903-.364 1.942h.212l.243-.242.985-1.306 1.652-2.064.73-.82.85-.904.547-.431h1.033l.76 1.129-.34 1.166-1.064 1.347-.881 1.142-1.264 1.7-.79 1.36.073.11.188-.02 2.856-.606 1.543-.28 1.841-.315.833.388.091.395-.328.807-1.969.486-2.309.462-3.439.813-.042.03.049.061 1.549.146.662.036h1.622l3.02.225.79.522.474.638-.079.485-1.215.62-1.64-.389-3.829-.91-1.312-.329h-.182v.11l1.093 1.068 2.006 1.81 2.509 2.33.127.578-.322.455-.34-.049-2.205-1.657-.851-.747-1.926-1.62h-.128v.17l.444.649 2.345 3.521.122 1.08-.17.353-.608.213-.668-.122-1.374-1.925-1.415-2.167-1.143-1.943-.14.08-.674 7.254-.316.37-.729.28-.607-.461-.322-.747.322-1.476.389-1.924.315-1.53.286-1.9.17-.632-.012-.042-.14.018-1.434 1.967-2.18 2.945-1.726 1.845-.414.164-.717-.37.067-.662.401-.589 2.388-3.036 1.44-1.882.93-1.086-.006-.158h-.055L4.132 18.56l-1.13.146-.487-.456.061-.746.231-.243 1.908-1.312z"),
    ("Perplexity", "https://www.perplexity.ai/search?q=", "M19.785 0v7.272H22.5V17.62h-2.935V24l-7.037-6.194v6.145h-1.091v-6.152L4.392 24v-6.465H1.5V7.188h2.884V0l7.053 6.494V.19h1.09v6.49L19.786 0zm-7.257 9.044v7.319l5.946 5.234V14.44l-5.946-5.397zm-1.099-.08l-5.946 5.398v7.235l5.946-5.234V8.965zm8.136 7.58h1.844V8.349H13.46l6.105 5.54v2.655zm-8.982-8.28H2.59v8.195h1.8v-2.576l6.192-5.62zM5.475 2.476v4.71h5.115l-5.115-4.71zm13.219 0l-5.115 4.71h5.115v-4.71z"),
    ("Google AI Mode", "https://www.google.com/search?udm=50&q=", "M23 12.245c0-.905-.075-1.565-.236-2.25h-10.54v4.083h6.186c-.124 1.014-.797 2.542-2.294 3.569l-.021.136 3.332 2.53.23.022C21.779 18.417 23 15.593 23 12.245z"),
    ("Grok", "https://grok.com/?q=", "M9.27 15.29l7.978-5.897c.391-.29.95-.177 1.137.272.98 2.369.542 5.215-1.41 7.169-1.951 1.954-4.667 2.382-7.149 1.406l-2.711 1.257c3.889 2.661 8.611 2.003 11.562-.953 2.341-2.344 3.066-5.539 2.388-8.42l.006.007c-.983-4.232.242-5.924 2.75-9.383.06-.082.12-.164.179-.248l-3.301 3.305v-.01L9.267 15.292M7.623 16.723c-2.792-2.67-2.31-6.801.071-9.184 1.761-1.763 4.647-2.483 7.166-1.425l2.705-1.25a7.808 7.808 0 00-1.829-1A8.975 8.975 0 005.984 5.83c-2.533 2.536-3.33 6.436-1.962 9.764 1.022 2.487-.653 4.246-2.34 6.022-.599.63-1.199 1.259-1.682 1.925l7.62-6.815"),
]
GOOGLE_EXTRA = (
    '<path d="M12.225 23c3.03 0 5.574-.978 7.433-2.665l-3.542-2.688c-.948.648-2.22 1.1-3.891 1.1a6.745 6.745 0 01-6.386-4.572l-.132.011-3.465 2.628-.045.124C4.043 20.531 7.835 23 12.225 23z"></path>'
    '<path d="M5.84 14.175A6.65 6.65 0 015.463 12c0-.758.138-1.491.361-2.175l-.006-.147-3.508-2.67-.115.054A10.831 10.831 0 001 12c0 1.772.436 3.447 1.197 4.938l3.642-2.763z"></path>'
    '<path d="M12.225 5.253c2.108 0 3.529.892 4.34 1.638l3.167-3.031C17.787 2.088 15.255 1 12.225 1 7.834 1 4.043 3.469 2.197 7.062l3.63 2.763a6.77 6.77 0 016.398-4.572z"></path>'
)
MARK = """<span class="brand-mark" aria-hidden="true"><img class="mark-light" src="/assets/icon/light.png" alt="" width="28" height="28"><img class="mark-dark" src="/assets/icon/dark.png" alt="" width="28" height="28"></span>"""
THEME = """<button class="theme-toggle" type="button" data-theme-toggle aria-label="Switch color theme"><svg class="moon" viewBox="0 0 24 24" aria-hidden="true"><path d="M20.5 14.2A8.5 8.5 0 0 1 9.8 3.5a8.5 8.5 0 1 0 10.7 10.7z"/></svg><svg class="sun" viewBox="0 0 24 24" aria-hidden="true"><circle cx="12" cy="12" r="4.2"/><path d="M12 2.5v2.2M12 19.3v2.2M2.5 12h2.2M19.3 12h2.2M5.3 5.3l1.6 1.6M17.1 17.1l1.6 1.6M5.3 18.7l1.6-1.6M17.1 6.9l1.6-1.6"/></svg></button>"""
MAIL = "mailto:hello@jabble.si?subject=Notchy"
GUIDES = [
    ("What is Notchy", "/blog/what-is-notchy/"),
    ("The glow", "/blog/the-glow/"),
    ("Open the panel", "/blog/open-the-panel/"),
    ("Screenshots", "/blog/screenshots/"),
    ("Recording", "/blog/screen-recording/"),
    ("Shortcuts", "/blog/shortcuts/"),
    ("Full-screen apps", "/blog/full-screen/"),
]
MORE_GUIDES = [
    ("Tools", "/blog/tools/"),
    ("Saved to Desktop", "/blog/saved-to-desktop/"),
    ("Other notch apps", "/blog/other-notch-apps/"),
    ("Dynamic Island for Mac", "/blog/dynamic-island-for-mac/"),
    ("NotchNook alternative", "/blog/notchnook-alternative/"),
    ("Scrolling screenshot", "/blog/scrolling-screenshot-mac/"),
]

POSTS = [
    {
        "slug": "what-is-notchy",
        "title": "What is Notchy?",
        "topic": "The notch",
        "topic_slug": "the-notch",
        "thumb": "notch",
        "date": "2026-10-24",
        "minutes": 3,
        "description": "Notchy is a Mac app that turns the notch at the top of the screen into a place for shortcuts, screenshots, recording and a few tools.",
        "quick": "Notchy lives in the notch. A glow brightens as the pointer gets close. Rest there, or click, and a panel drops down for shortcuts, screenshots, recording and tools.",
        "sections": [
            ("key-points", "Key points", """
<ul>
<li>Notchy is a Mac app. It uses the notch at the top of the screen.</li>
<li>The glow is a soft light. It gets brighter as the pointer gets closer.</li>
<li>Amber means something needs approval. Green means it is done.</li>
<li>The panel holds shortcuts, screenshots, recording, tools, Settings and Quit.</li>
<li>The notch on this website is a preview. It does not capture your screen.</li>
</ul>"""),
            ("what-it-does", "What it does", """
<p>The notch is usually a camera housing and a clock. Notchy makes it a control you can reach without hunting through menus. Bring the pointer near it and a soft light appears. Rest the pointer on it, or click it, and the panel drops down.</p>
<p>From that panel you can open the shortcuts you chose, take a screenshot, start a recording, or use a tool such as the focus timer. Finder, Safari and Terminal are the shortcuts at the start. You choose the rest.</p>"""),
            ("what-this-page-is", "What this page is", """
<p>The black screen at the top of the home page behaves like the notch: the glow tracks the pointer, and a click or a rest opens the panel. The buttons explain the same actions. They do not shoot the screen, record it, or turn a camera on.</p>
<p>The Mac app is the one that does those things. Write to <a href="mailto:hello@jabble.si">hello@jabble.si</a> to ask for it. This site does not take payment.</p>"""),
        ],
    },
    {
        "slug": "dynamic-island-for-mac",
        "title": "Dynamic Island for Mac",
        "topic": "The notch",
        "topic_slug": "the-notch",
        "thumb": "notch",
        "date": "2026-11-02",
        "minutes": 3,
        "description": "Dynamic Island for Mac is what people type when they want the MacBook notch to act like the iPhone island. That is a different job from Notchy.",
        "quick": "A Dynamic Island for Mac is a notch app that behaves like the iPhone island, usually for music or whatever is happening now. Alcove is built for that. Notchy uses the notch for a screenshot and a recording.",
        "sections": [
            ("what-the-phrase-means", "What the phrase means", """
<p>People search "Dynamic Island for Mac" when they want the black cutout on a MacBook to wake up the way the island does on an iPhone. Music. A timer. Something that just happened.</p>
<p>That is a real group of apps. <a href="https://tryalcove.com/" target="_blank" rel="noopener">Alcove<span class="vh"> (opens in a new tab)</span></a> calls itself a Dynamic Island for the Mac. <a href="https://getnotchnook.com/" target="_blank" rel="noopener">NotchNook<span class="vh"> (opens in a new tab)</span></a> and <a href="https://github.com/TheBoredTeam/boring.notch" target="_blank" rel="noopener">Boring Notch<span class="vh"> (opens in a new tab)</span></a> put music, a calendar, and a file tray in the same spot. <a href="/blog/other-notch-apps/">What else lives in the notch</a> goes through those three.</p>"""),
            ("not-the-same-search", "Not the same search as a screenshot", """
<p>Notchy is not that island. There is no now-playing control and no visualizer. A glow brightens as the pointer gets close. Rest on the notch, or click it, and the panel drops down with your shortcuts, a screenshot, and a recording.</p>
<p>If the phrase you typed was the iPhone island, start with the app that says so on its own site. If the phrase you wanted was a shot or a recording from the top of the screen, this is the panel for that.</p>"""),
        ],
    },
    {
        "slug": "notchnook-alternative",
        "title": "A NotchNook alternative",
        "topic": "The app",
        "topic_slug": "the-app",
        "thumb": "app",
        "date": "2026-11-02",
        "minutes": 3,
        "description": "A NotchNook alternative only helps if you wanted a different job. NotchNook is music, files, and a calendar. Notchy is the screenshot and the recording.",
        "quick": "NotchNook alternative, Boring Notch alternative, and Alcove alternative are the same search. Those apps are music, files, and a calendar. Notchy is the alternative when the job is a screenshot or a recording.",
        "sections": [
            ("which-part", "Which part you actually wanted", """
<p>"NotchNook alternative" shows up next to "Boring Notch alternative" and "Alcove alternative." Someone tried a notch app, or read about one, and wants another. The useful split is the job.</p>
<p>On its own site, NotchNook Pro is music, a calendar, files, a teleprompter, and AI agents. Classic is media controls, Calendar, widgets, and a file tray. Boring Notch describes music with a visualizer, a calendar, a file shelf that can AirDrop, and the Mac's volume and brightness display. Alcove presents itself as a Dynamic Island for the Mac.</p>
<p>Notchy does not play the song in the notch, and it does not try to be that island.</p>"""),
            ("when-it-is-notchy", "When the alternative is Notchy", """
<p>Notchy is the one to look at when the job is the screen. Screenshot the whole screen, an area, or a long scrolling page. Record the screen or an area, with a timer and Stop. A 25 minute focus timer, a drop shelf, copy text, a color picker, and Scan QR sit in the same panel.</p>
<p>If you wanted the file tray and the music controls, NotchNook or Boring Notch is the closer match. Their pages are where to read the price and the current list. This site does not sell a license.</p>"""),
        ],
    },
    {
        "slug": "scrolling-screenshot-mac",
        "title": "Scrolling screenshot on a Mac",
        "topic": "Capture",
        "topic_slug": "capture",
        "thumb": "capture",
        "date": "2026-11-02",
        "minutes": 2,
        "description": "A scrolling screenshot is one long image of a page that does not fit on the Mac screen. Notchy's Scroll button is that shot.",
        "quick": "A scrolling screenshot on a Mac is one image of a page that runs past the bottom of the window. Shift Command 3 and 4 do not do that. In Notchy it is Scroll, and Control Option Command 7.",
        "sections": [
            ("the-long-page", "The page that does not fit", """
<p>People search "scrolling screenshot Mac," "capture a long page," or "full page screenshot Mac" when one picture of the screen cuts the page in half. A chat, a document, or a web page keeps going. The shot they want is the whole of it, stitched into one image.</p>
<p>Shift Command 3 takes the screen. Shift Command 4 takes an area. Shift Command 5 opens the Mac's own panel. None of those follow the page as it moves. <a href="/blog/mac-already-screenshots/">The Mac already takes the shot</a> is that set of keys.</p>"""),
            ("scroll-in-notchy", "Scroll, in the notch", """
<p>In Notchy the button is Scroll. It sits with Screen and Area. The keys are <kbd>Ctrl</kbd><kbd>Opt</kbd><kbd>Cmd</kbd><kbd>7</kbd>. When the shot finishes, the glow pulses green, and the panel can say it was saved to the Desktop, with Show in Finder.</p>
<p>The button on this website is a preview. It does not capture the page you are reading. The Mac app is the one that does.</p>"""),
        ],
    },
    {
        "slug": "what-is-the-macbook-notch",
        "title": "What is the MacBook notch for?",
        "topic": "The notch",
        "topic_slug": "the-notch",
        "thumb": "notch",
        "date": "2026-11-02",
        "minutes": 3,
        "description": "The MacBook notch is the camera housing at the top of the screen. It is not a button until an app makes it one.",
        "quick": "The MacBook notch is the black cutout around the camera. On its own it does nothing you can click. Some apps hide it. Notchy turns it into a panel for a screenshot, a recording, and a few tools.",
        "sections": [
            ("the-cutout", "The cutout", """
<p>"What is the MacBook notch" and "what is the notch for" are the searches from a new machine. The display runs around the camera. The black shape in the menu bar is that housing. It is not a control by itself.</p>
<p>A related search is "hide MacBook notch." Some utilities extend a black menu bar so the cutout blends in and looks gone. That gives you the menu bar you already had. It does not add a panel.</p>"""),
            ("making-it-a-control", "Making it a control", """
<p>A notch app puts a job in that housing. The ones people find first put music, files, or a calendar there. <a href="/blog/dynamic-island-for-mac/">Dynamic Island for Mac</a> is the name of that search.</p>
<p>Notchy puts a glow there. It gets brighter as the pointer gets closer. Rest on the notch, or click it, and a panel drops down: shortcuts, a screenshot, a recording, and tools such as a 25 minute focus timer. In a full-screen app the glow stays off, and only a click opens the panel.</p>"""),
        ],
    },
    {
        "slug": "record-your-mac-screen",
        "title": "How to record your Mac screen",
        "topic": "Capture",
        "topic_slug": "capture",
        "thumb": "capture",
        "date": "2026-11-02",
        "minutes": 2,
        "description": "Shift Command 5 opens the Mac's own screen recorder. Notchy records from the notch, with a timer and Stop.",
        "quick": "To record your Mac screen, press Shift Command 5 and pick the record button. Notchy does the same job from the notch: Control Option Command 5 for the whole screen, 6 for an area.",
        "sections": [
            ("the-built-in-way", "The way the Mac already records", """
<p>"How to record my Mac screen" and "screen record on Mac" are the searches. The built-in answer is Shift Command 5. That panel has a record control for the whole screen and one for an area you select. Notchy does not turn those keys off.</p>"""),
            ("from-the-notch", "From the notch instead", """
<p>Notchy puts those two choices on the notch. Record Screen and Record Area are in the panel. <kbd>Ctrl</kbd><kbd>Opt</kbd><kbd>Cmd</kbd><kbd>5</kbd> starts and stops the screen. <kbd>Ctrl</kbd><kbd>Opt</kbd><kbd>Cmd</kbd><kbd>6</kbd> starts and stops the area. While it runs, the control shows the time and Stop.</p>
<p>The glow pulses amber if the Mac still has to allow the recording, and green when it stops. <a href="/blog/screen-recording/">Record the screen from the notch</a> is the longer note.</p>"""),
        ],
    },
    {
        "slug": "focus-timer-mac",
        "title": "A focus timer on the Mac",
        "topic": "Tools",
        "topic_slug": "tools",
        "thumb": "tools",
        "date": "2026-11-02",
        "minutes": 2,
        "description": "A focus timer on the Mac can sit in the notch. Notchy's starts at 25 minutes and counts down in the panel.",
        "quick": "People search for a Pomodoro timer or a menu bar timer on the Mac. Notchy's focus timer starts at 25 minutes, in the notch panel, next to the screenshot and the recording.",
        "sections": [
            ("the-search", "Pomodoro, menu bar timer, focus timer", """
<p>Those three phrases are one job: a block of time, then a stop. Notchy's block starts at 25 minutes. In the tools row the button reads "25 min" until it is running, then it counts down.</p>
<p>It does not keep a history, and it does not schedule the break after the block. It is the 25 minutes.</p>"""),
            ("where-it-sits", "It sits in the notch", """
<p>You do not keep a separate timer in the Dock. Open the notch and it is in the tools row, beside Shelf, Copy Text, Color, and Scan QR. Starting it does not take a screenshot. The capture buttons stay next to it.</p>
<p><a href="/blog/tools/">Tools in the notch panel</a> lists the rest of that row, including the ones you can leave off.</p>"""),
        ],
    },
    {
        "slug": "other-notch-apps",
        "title": "What else lives in the notch",
        "topic": "The app",
        "topic_slug": "the-app",
        "thumb": "app",
        "date": "2026-11-02",
        "minutes": 4,
        "description": "NotchNook, Alcove and Boring Notch already use the Mac notch. They are mostly music, files and a calendar. Notchy is the glow, the shot and the recording.",
        "quick": "NotchNook, Alcove and Boring Notch already live in the Mac notch. They lean on music, files and a calendar. Notchy is the glow, your shortcuts, the screenshot and the recording.",
        "sections": [
            ("the-group", "Three apps people already name", """
<p>Search for a notch app and the same names come up. They are not copies of each other. Each one picked a job.</p>
<p><a href="https://getnotchnook.com/" target="_blank" rel="noopener">NotchNook<span class="vh"> (opens in a new tab)</span></a>, from lo.cafe, calls itself the original notch app. On their site, NotchNook Pro is music, a calendar, files, a teleprompter and AI agents. Classic is media controls, Calendar, widgets and a file tray. They offer a 48-hour try, and they say notes, files and anything from the camera stay on the Mac.</p>
<p><a href="https://tryalcove.com/" target="_blank" rel="noopener">Alcove<span class="vh"> (opens in a new tab)</span></a> presents itself as a Dynamic Island for the Mac. That is the iPhone idea: the notch shows what is happening now, instead of holding a tray of files.</p>
<p><a href="https://github.com/TheBoredTeam/boring.notch" target="_blank" rel="noopener">Boring Notch<span class="vh"> (opens in a new tab)</span></a> is an open-source project under GPL-3.0, with a page at <a href="https://theboring.name/" target="_blank" rel="noopener">theboring.name<span class="vh"> (opens in a new tab)</span></a>. The project describes a music control with a visualizer, a calendar, a file shelf that can AirDrop, and a replacement for the Mac's volume and brightness display.</p>"""),
            ("where-notchy-fits", "Where Notchy fits", """
<p>Notchy is not a music player, and it is not a dashboard of widgets. A soft glow brightens as the pointer gets close to the notch. Rest there, or click, and the panel drops down.</p>
<p>In that panel: the shortcuts you chose, a screenshot of the whole screen, an area, or a long scrolling page, and a recording of the screen or an area with a timer and Stop. The tool row is short. It is a 25-minute focus timer, a drop shelf, copy text, a color picker and Scan QR. Keep awake, a world clock, a camera mirror, Downloads alerts and the next meeting can be turned on. They are not the front of the panel.</p>
<p>A place to drop a file shows up often in this group. In Notchy the shelf is one tool in that row, not the reason for the app.</p>
<p>This site does not name a price and does not take payment. The other apps set their own. Their pages are the place to read what they charge today.</p>"""),
        ],
    },
    {
        "slug": "music-or-capture",
        "title": "Music, a file tray, or a capture",
        "topic": "The notch",
        "topic_slug": "the-notch",
        "thumb": "notch",
        "date": "2026-11-02",
        "minutes": 3,
        "description": "Most notch apps are a now-playing control and a place to drop files. Notchy is for taking the screen and recording it from that same spot.",
        "quick": "The notch apps that came first are mostly now-playing and a file tray. Notchy takes the other job: a screenshot and a recording, from the notch.",
        "sections": [
            ("two-jobs", "The jobs that repeat", """
<p>Read across <a href="/blog/other-notch-apps/">NotchNook, Alcove and Boring Notch</a> and two jobs keep showing up. One is music: what is playing, and a control for it. The other is files: drag something into the notch and pick it up later. Boring Notch and NotchNook both talk about that tray. NotchNook's can sit next to a calendar and widgets. Alcove aims the same piece of screen at what is happening now, in the style of the iPhone's Dynamic Island.</p>
<p>A third job is capture. <a href="https://quackscreen.com/" target="_blank" rel="noopener">QuackScreen<span class="vh"> (opens in a new tab)</span></a> is one of the apps that takes it: their site describes a short recording from the notch, capped at three minutes, on macOS 26 and Apple silicon, plus a screenshot you can drag out of the notch.</p>"""),
            ("the-job-notchy-takes", "The job Notchy takes", """
<p>Notchy is that third job, without a song visualizer. Screen, Area and Scroll are the screenshots. Screen and Area are the recordings, with a timer and Stop. The keys are <kbd>Ctrl</kbd><kbd>Opt</kbd><kbd>Cmd</kbd><kbd>3</kbd>, <kbd>4</kbd> and <kbd>7</kbd> for shots, and <kbd>5</kbd> and <kbd>6</kbd> for recordings. <a href="/blog/shortcuts/">The shortcut list</a> is the full set.</p>
<p>The glow is how you know the notch noticed the pointer. It pulses amber when something needs approval, which a capture often does, because the Mac asks first. It pulses green when that thing is done.</p>
<p>If you want the song that is playing drawn in the notch, one of the other apps is built for that. If you want the shot and the recording without leaving the top of the screen, that is what this panel is for.</p>"""),
        ],
    },
    {
        "slug": "mac-already-screenshots",
        "title": "The Mac already takes the shot",
        "topic": "Capture",
        "topic_slug": "capture",
        "thumb": "capture",
        "date": "2026-11-02",
        "minutes": 3,
        "description": "Shift Command 3, 4 and 5 are still the Mac's own screenshot keys. Notchy adds the notch, a scrolling shot, and a recording beside them.",
        "quick": "Shift Command 3, 4 and 5 stay the Mac's own screenshot keys. Notchy does not turn them off. It adds the notch, a scrolling page, and a recording with a timer.",
        "sections": [
            ("apples-keys", "The keys Apple already gave you", """
<p>You do not need another app to take a screenshot. Shift Command 3 takes the whole screen. Shift Command 4 takes an area, and the Space bar turns that into a window. Shift Command 5 opens the Mac's own screenshot panel, which can also start a recording.</p>
<p>Those keys stay yours. Notchy does not replace them and does not turn them off.</p>"""),
            ("what-the-notch-adds", "What the notch adds", """
<p>Notchy puts the same kind of work on the notch, with its own chords so the two sets do not collide. <kbd>Ctrl</kbd><kbd>Opt</kbd><kbd>Cmd</kbd><kbd>3</kbd>, <kbd>4</kbd> and <kbd>7</kbd> are the screen, an area, and a long scrolling page. <kbd>Ctrl</kbd><kbd>Opt</kbd><kbd>Cmd</kbd><kbd>5</kbd> and <kbd>6</kbd> start and stop a recording of the screen or an area.</p>
<p>The scrolling page is the one the standard keys do not offer as a button. The recording shows a timer and Stop in the panel. The glow pulses amber if the Mac still has to allow the capture, and green when it finishes. A finished shot can say it was saved to the Desktop, with Show in Finder.</p>
<p>A dedicated capture app, the kind with a full set of markup tools, is a deeper editor after the fact. Notchy is where the shot starts. <a href="/blog/screenshots/">Screenshots from the notch</a> walks through Screen, Area and Scroll.</p>"""),
        ],
    },
    {
        "slug": "the-glow",
        "title": "The glow around the notch",
        "topic": "The notch",
        "topic_slug": "the-notch",
        "thumb": "notch",
        "date": "2026-10-25",
        "minutes": 2,
        "description": "A soft light appears around the notch as the pointer gets near, and it gets brighter the closer it gets.",
        "quick": "The glow tracks distance. Farther away it is faint. Closer, it is brighter. It pulses amber when something needs approval and green when that thing is done.",
        "sections": [
            ("distance", "Brighter as you get closer", """
<p>Move the pointer toward the notch and a soft light shows up around it. The light is not a switch. It strengthens as the pointer closes in, so you can see that Notchy noticed you before the panel opens.</p>
<p>On the home page preview, the line under the screen shows the glow as a percent. That number is only for the preview. The Mac app shows the light itself.</p>"""),
            ("amber-and-green", "Amber and green", """
<p>The same light has two signals. It pulses amber when something needs approval. It pulses green when that thing is done. A screenshot finishing is one of those done moments. Starting a recording can be one of the approval moments, because the Mac may ask before a capture.</p>
<p>In a full-screen app the glow stays off, so it does not sit on top of that app's own menus. <a href="/blog/full-screen/">Full-screen apps</a> explains the click that still opens the panel.</p>"""),
        ],
    },
    {
        "slug": "open-the-panel",
        "title": "Open the panel from the notch",
        "topic": "The notch",
        "topic_slug": "the-notch",
        "thumb": "notch",
        "date": "2026-10-26",
        "minutes": 2,
        "description": "Rest the pointer on the notch, or click it, and the panel drops down.",
        "quick": "Rest the pointer on the notch or click it. The panel drops down with your shortcuts, screenshots, recording, tools, Settings and Quit.",
        "sections": [
            ("two-ways", "Two ways to open it", """
<p>Bring the pointer onto the notch and let it rest there. The panel drops down. A click on the notch does the same thing, which is the way that still works when a full-screen app has turned the glow off.</p>
<p>The top of the panel is your shortcuts. Finder, Safari and Terminal are there unless you have changed them. Under that are screenshots, recording and tools. Settings and Quit sit at the corners.</p>"""),
            ("what-is-inside", "What is inside", """
<ul>
<li>Shortcuts you chose. Finder, Safari and Terminal by default.</li>
<li>Screenshot: the whole screen, an area, or a long scrolling page.</li>
<li>Record: the whole screen or an area, with a timer and Stop.</li>
<li>Tools: focus timer, drop shelf, copy text, Scan QR, color picker, keep awake, world clock, and optional camera mirror, Downloads alerts and next meeting.</li>
</ul>
<p>The preview on the home page opens the same panel. Its buttons do not leave this page.</p>"""),
        ],
    },
    {
        "slug": "screenshots",
        "title": "Screenshots from the notch",
        "topic": "Capture",
        "topic_slug": "capture",
        "thumb": "capture",
        "date": "2026-10-27",
        "minutes": 3,
        "description": "Notchy takes a screenshot of the whole screen, an area, or a long scrolling page, from the notch or with a shortcut.",
        "quick": "Three shots: the whole screen, an area, or a scrolling page. The panel buttons are Screen, Area and Scroll. The keys are Control Option Command 3, 4 and 7.",
        "sections": [
            ("three-shots", "Three shots", """
<p>Screen grabs the whole screen. Area grabs the part you choose. Scroll follows a long page, the kind that does not fit in one view.</p>
<p>Each one is in the panel, and each one has a shortcut: <kbd>Ctrl</kbd><kbd>Opt</kbd><kbd>Cmd</kbd><kbd>3</kbd> for the screen, <kbd>Ctrl</kbd><kbd>Opt</kbd><kbd>Cmd</kbd><kbd>4</kbd> for an area, <kbd>Ctrl</kbd><kbd>Opt</kbd><kbd>Cmd</kbd><kbd>7</kbd> for the scrolling page.</p>"""),
            ("after-the-shot", "After the shot", """
<p>When a shot finishes, the glow pulses green. The panel can report that the screenshot was saved to the Desktop, with Show in Finder beside that line. The preview on this website shows the same words and does not write a file.</p>
<p>Copy text and the color picker are separate tools. They are not screenshots. <a href="/blog/tools/">Tools in the panel</a> covers them.</p>"""),
        ],
    },
    {
        "slug": "screen-recording",
        "title": "Record the screen from the notch",
        "topic": "Capture",
        "topic_slug": "capture",
        "thumb": "capture",
        "date": "2026-10-28",
        "minutes": 2,
        "description": "Record the whole screen or an area from the notch. A timer runs until you stop.",
        "quick": "Record the whole screen or an area. The panel shows a timer and Stop. Control Option Command 5 and 6 start and stop those recordings.",
        "sections": [
            ("screen-or-area", "Screen or area", """
<p>The record row has two buttons: Screen and Area. Screen records the whole screen. Area records the part you choose. While a recording is going, the control shows a timer and Stop.</p>
<p><kbd>Ctrl</kbd><kbd>Opt</kbd><kbd>Cmd</kbd><kbd>5</kbd> starts and stops a recording of the screen. <kbd>Ctrl</kbd><kbd>Opt</kbd><kbd>Cmd</kbd><kbd>6</kbd> starts and stops a recording of an area.</p>"""),
            ("approval", "When the Mac asks", """
<p>A capture can need approval. The glow pulses amber for that, and green when the thing is done. Stopping a recording is one of the done moments.</p>
<p>The home page preview plays the amber pulse, then the timer, then a green pulse when you hit Stop. It does not record your screen.</p>"""),
        ],
    },
    {
        "slug": "shortcuts",
        "title": "Keyboard shortcuts for the notch",
        "topic": "Capture",
        "topic_slug": "capture",
        "thumb": "capture",
        "date": "2026-10-29",
        "minutes": 2,
        "description": "Control Option Command 3, 4 and 7 take screenshots. 5 and 6 start and stop recordings.",
        "quick": "Hold Control, Option and Command, then press 3, 4 or 7 for a screenshot, or 5 or 6 for a recording.",
        "sections": [
            ("the-keys", "The keys", """
<ul>
<li><kbd>Ctrl</kbd><kbd>Opt</kbd><kbd>Cmd</kbd><kbd>3</kbd> screenshots the whole screen.</li>
<li><kbd>Ctrl</kbd><kbd>Opt</kbd><kbd>Cmd</kbd><kbd>4</kbd> screenshots an area.</li>
<li><kbd>Ctrl</kbd><kbd>Opt</kbd><kbd>Cmd</kbd><kbd>7</kbd> screenshots a long scrolling page.</li>
<li><kbd>Ctrl</kbd><kbd>Opt</kbd><kbd>Cmd</kbd><kbd>5</kbd> starts and stops a recording of the screen.</li>
<li><kbd>Ctrl</kbd><kbd>Opt</kbd><kbd>Cmd</kbd><kbd>6</kbd> starts and stops a recording of an area.</li>
</ul>
<p>On the home page, those same chords run the preview if the browser receives them. They still do not capture the screen.</p>"""),
            ("the-panel", "The panel does the same jobs", """
<p>You do not need the keys. Screen, Area and Scroll sit in the screenshot row. Screen and Area sit in the record row, and Stop shows up on the one that is running.</p>"""),
        ],
    },
    {
        "slug": "full-screen",
        "title": "Full-screen apps and the glow",
        "topic": "The app",
        "topic_slug": "the-app",
        "thumb": "app",
        "date": "2026-10-30",
        "minutes": 2,
        "description": "In a full-screen app the glow stays off. Only a click opens the panel.",
        "quick": "When an app is full screen, Notchy keeps the glow off so it does not cover that app's menus. Click the notch to open the panel.",
        "sections": [
            ("why-it-stays-off", "Why it stays off", """
<p>A full-screen app puts its own menus along the top. A glow there would get in the way. Notchy leaves the glow off for that case.</p>
<p>The panel is still there. Click the notch and it drops down. Resting the pointer on the notch does not open it while the glow is off.</p>"""),
            ("try-it", "Try it on this page", """
<p>The home page has a Full-screen app switch under the preview. Turn it on and the glow stops tracking the pointer. Click the notch and the panel still opens. Turn the switch off and the glow comes back.</p>"""),
        ],
    },
    {
        "slug": "tools",
        "title": "Tools in the notch panel",
        "topic": "Tools",
        "topic_slug": "tools",
        "thumb": "tools",
        "date": "2026-10-31",
        "minutes": 3,
        "description": "Focus timer, drop shelf, copy text, Scan QR, color picker, keep awake, world clock, and three optional tools.",
        "quick": "The tools row holds a focus timer, a drop shelf, copy text, Scan QR and a color picker, plus keep awake and a world clock. Camera mirror, Downloads alerts and next meeting are optional.",
        "sections": [
            ("always-there", "The tools", """
<ul>
<li>Focus timer. The panel shows it as 25 minutes, and it counts down.</li>
<li>Drop shelf. A place to leave something for a moment.</li>
<li>Copy text. It reads type that is on the screen.</li>
<li>Scan QR. It reads a code that is on the screen.</li>
<li>Color picker. It reads the color under the pointer.</li>
<li>Keep awake. It keeps the Mac from sleeping.</li>
<li>World clock. Times in other places.</li>
</ul>"""),
            ("optional", "Optional", """
<p>Three more can be turned on: a camera mirror, Downloads alerts, and the next meeting. They are optional, so the panel does not have to show them.</p>
<p>Settings is where those choices live, next to Quit. The preview on the home page labels each of these and does not use your camera, your Downloads folder, or a calendar.</p>"""),
        ],
    },
    {
        "slug": "saved-to-desktop",
        "title": "Where a screenshot goes",
        "topic": "The app",
        "topic_slug": "the-app",
        "thumb": "app",
        "date": "2026-11-01",
        "minutes": 2,
        "description": "After a screenshot, the panel can say it was saved to the Desktop and offer Show in Finder.",
        "quick": "A finished screenshot can show “Screenshot saved to Desktop” in the panel, with Show in Finder. The website preview shows that line and does not write a file.",
        "sections": [
            ("the-line", "The line in the panel", """
<p>When a shot is done, the glow pulses green and the panel can show a green dot with the words “Screenshot saved to Desktop”, plus Show in Finder. That is the file on your Mac, in the Desktop folder.</p>
<p>This website repeats the sentence so you can see where the line sits. Pressing the preview button does not create an image and does not open Finder.</p>"""),
            ("not-a-library", "Not a library on this site", """
<p>There is no account on this website and no place here to upload a shot. The home page says so under the preview. Email to <a href="mailto:hello@jabble.si">hello@jabble.si</a> is the message you send. It is not a screenshot.</p>"""),
        ],
    },
]


def esc(value):
    return html.escape(value, quote=True)


def pretty_date(iso):
    return datetime.strptime(iso, "%Y-%m-%d").strftime("%B %-d, %Y")


def ask_html():
    from urllib.parse import quote
    bits = []
    for name, base, path in ASK:
        extra = GOOGLE_EXTRA if name == "Google AI Mode" else ""
        href = base + quote(Q)
        bits.append(
            f'<a href="{esc(href)}" target="_blank" rel="noopener">'
            f'<svg class="ai-logo" aria-hidden="true" focusable="false" fill="currentColor" fill-rule="evenodd" viewBox="0 0 24 24"><path d="{path}"></path>{extra}</svg>'
            f'{esc(name)}<span class="vh"> (opens in a new tab)</span></a>'
        )
    return f'<div class="ask"><p>Ask AI about Notchy</p><div class="ask-links">{"".join(bits)}</div></div>'


def footer():
    guides = "".join(f'<li><a href="{href}">{esc(name)}</a></li>' for name, href in GUIDES)
    more = "".join(f'<li><a href="{href}">{esc(name)}</a></li>' for name, href in MORE_GUIDES)
    return f"""<footer>
  <div class="frame">
    {ask_html()}
    <div class="foot-cols">
      <div class="foot-brand">
        <a class="brand" href="/">{MARK}Notchy</a>
        <p class="of">A product of <a href="https://jabble.si/" target="_blank" rel="noopener">jabble.si<span class="vh"> (opens in a new tab)</span></a></p>
      </div>
      <div>
        <h2>Notchy</h2>
        <ul>
          <li><a href="/#glow">Glow</a></li>
          <li><a href="/#panel-feature">Panel</a></li>
          <li><a href="/#screenshots">Screenshots</a></li>
          <li><a href="/#record">Record</a></li>
          <li><a href="/#tools">Tools</a></li>
          <li><a href="/#questions">Questions</a></li>
          <li><a href="/blog/">Blog</a></li>
        </ul>
      </div>
      <div>
        <h2>Guides</h2>
        <ul>{guides}</ul>
        <button type="button" class="more" aria-expanded="false" aria-controls="more-guides">More</button>
        <ul id="more-guides" class="foot-more-rest" hidden>{more}</ul>
      </div>
      <div>
        <h2>Support</h2>
        <ul>
          <li><a href="mailto:hello@jabble.si">hello@jabble.si</a></li>
          <li><a href="/#questions">Questions</a></li>
          <li><a href="/privacy.html">Privacy</a></li>
          <li><a href="/terms.html">Terms</a></li>
          <li><a href="/license.html">License</a></li>
          <li><a href="/refunds.html">Refunds</a></li>
          <li><a href="/your-data.html">Your data</a></li>
        </ul>
      </div>
      <div>
        <h2>More apps</h2>
        <ul>
          <li><a href="https://trybondi.app/" target="_blank" rel="noopener">Bondi for Mac<span class="vh"> (opens in a new tab)</span></a></li>
          <li><a href="https://wigglemac.com/" target="_blank" rel="noopener">Wiggle for Mac<span class="vh"> (opens in a new tab)</span></a></li>
        </ul>
      </div>
    </div>
    <div class="credit">
      <p>Notchy turns the notch on your Mac into shortcuts, screenshots, recording and tools.</p>
      <p class="maker">Made with <span class="heart" role="img" aria-label="love">♥</span> by Noaman</p>
    </div>
    <div class="legal-line">
      <p>© 2026 Jabble Super Intelligence Inc.</p>
      <p class="mark">Apple, Mac, macOS and Finder are trademarks of Apple Inc. Notchy isn't made or endorsed by Apple.</p>
    </div>
  </div>
</footer>"""


def header(blog_current=False):
    blog = ' aria-current="page"' if blog_current else ""
    return f"""<header class="site-head">
  <div class="frame head">
    <a class="brand" href="/">{MARK}Notchy</a>
    <nav class="head-nav" aria-label="Main">
      <a href="/#glow">Glow</a>
      <a href="/#panel-feature">Panel</a>
      <a href="/#screenshots">Screenshots</a>
      <a href="/#record">Record</a>
      <a href="/blog/"{blog}>Blog</a>
      <a class="pill primary small" href="{MAIL}">Get Notchy</a>
      {THEME}
    </nav>
  </div>
</header>"""


def shell(title, description, body, blog=False, blog_current=False):
    css = '<link rel="stylesheet" href="/styles.css?v=20261103">'
    if blog:
        css += '\n<link rel="stylesheet" href="/blog.css?v=20261103">'
        css += '\n<link rel="alternate" type="application/rss+xml" title="Notchy blog" href="/blog/rss.xml">'
    return f"""<!doctype html>
<html lang="en">
<head>
<meta charset="utf-8">
<meta name="viewport" content="width=device-width, initial-scale=1">
<title>{esc(title)}</title>
<meta name="description" content="{esc(description)}">
<meta name="theme-color" content="#ffffff" media="(prefers-color-scheme: light)">
<meta name="theme-color" content="#131315" media="(prefers-color-scheme: dark)">
<link rel="icon" id="favicon" href="/assets/icon/favicon-light.png">
<link rel="apple-touch-icon" href="/assets/icon/apple-touch-light.png">
{css}
<script>
(function () {{
  var theme = null;
  try {{ theme = localStorage.getItem("theme"); }} catch (e) {{}}
  if (theme === "light" || theme === "dark") document.documentElement.dataset.theme = theme;
  var dark = theme === "dark" || (theme !== "light" && matchMedia("(prefers-color-scheme: dark)").matches);
  var fav = document.getElementById("favicon");
  if (fav) fav.href = dark ? "/assets/icon/favicon-dark.png" : "/assets/icon/favicon-light.png";
}})();
</script>
</head>
<body>
{header(blog_current)}
{body}
{footer()}
<script src="/site.js"></script>
</body>
</html>
"""


def write(path, text):
    dest = ROOT / path
    dest.parent.mkdir(parents=True, exist_ok=True)
    dest.write_text(text, encoding="utf-8")


def icon(path):
    return f'<svg viewBox="0 0 24 24" aria-hidden="true">{path}</svg>'


RECT = '<rect x="4" y="5" width="16" height="12" rx="2" fill="none" stroke="currentColor" stroke-width="1.7"/>'
HOME = f"""
<main>
  <section class="hero">
    <div class="frame">
      <div class="hero-icon" aria-hidden="true"><img class="mark-light" src="/assets/icon/light-pointer.png" alt="" width="128" height="128"><img class="mark-dark" src="/assets/icon/dark-pointer.png" alt="" width="128" height="128"></div>
      <p class="eyebrow">For Mac</p>
      <h1>Screenshot, record, focus. All from the notch.</h1>
      <p class="lede">Notchy is your own Mac app. It turns the notch at the top of the screen into something you can use. A soft light appears as your pointer gets near, and it gets brighter the closer it gets.</p>
      <div class="cta-row">
        <a class="pill primary" href="{MAIL}">Get Notchy</a>
        <a class="pill secondary" href="#notch-demo">Try the notch</a>
      </div>
    </div>
  </section>
  <section class="stage-section" id="notch-demo">
    <div class="frame">
      <div class="modes" role="tablist" aria-label="Preview">
        <button type="button" role="tab" aria-selected="true" data-mode="glow">Glow</button>
        <button type="button" role="tab" aria-selected="false" data-mode="panel">Panel</button>
        <button type="button" role="tab" aria-selected="false" data-mode="shot">Screenshot</button>
        <button type="button" role="tab" aria-selected="false" data-mode="rec">Record</button>
        <button type="button" role="tab" aria-selected="false" data-mode="tools">Tools</button>
        <button type="button" role="tab" aria-selected="false" data-mode="full">Full screen</button>
      </div>
      <div class="mac" id="mac">
        <div class="menubar">
          <div class="menu-left">
            <svg class="apple" viewBox="0 0 14 16" aria-hidden="true"><path fill="currentColor" d="M11.2 8.4c0-1.8 1.5-2.7 1.6-2.8-0.9-1.3-2.2-1.4-2.7-1.5-1.1-0.1-2.2.7-2.8.7s-1.5-.7-2.4-.6c-1.2 0-2.4.7-3 1.9-1.3 2.2-.3 5.5.9 7.3.6.9 1.3 1.9 2.3 1.8 0.9 0 1.3-.6 2.4-.6s1.4.6 2.4.6 1.6-.9 2.2-1.8c.7-1 1-2 1-2.1-.1 0-1.9-.7-1.9-2.9zM9.4 3.2c.5-.6.8-1.4.7-2.2-.7 0-1.5.5-2 .1C7.6 1.6 7.2 2.4 7.3 3.2c.8.1 1.6-.4 2.1-1z"/></svg>
            <span>Finder</span>
            <span class="hide-sm">File</span>
            <span class="hide-sm">Edit</span>
            <span class="hide-sm">View</span>
          </div>
          <div class="menu-right"><span id="menu-clock" class="hide-sm"></span></div>
        </div>
        <div class="notch-wrap" id="notch">
          <div class="glow" id="glow" aria-hidden="true"></div>
          <button type="button" class="notch-hit" id="notch-hit" aria-expanded="false" aria-controls="panel"><span class="cam" aria-hidden="true"></span><span class="vh">Notchy</span></button>
          <div class="panel" id="panel" role="dialog" aria-label="Notchy" aria-hidden="true">
            <button type="button" class="gear" data-act="settings" aria-label="Settings"><img src="/assets/panel/gear.png" alt=""></button>
            <div class="apps" data-group="panel" aria-label="Shortcuts">
              <button type="button" class="app" data-act="app" data-name="Finder" aria-label="Finder"><img src="/assets/panel/app-0.png" alt=""></button>
              <button type="button" class="app" data-act="app" data-name="Safari" aria-label="Safari"><img src="/assets/panel/app-1.png" alt=""></button>
              <button type="button" class="app" data-act="app" data-name="Terminal" aria-label="Terminal"><img src="/assets/panel/app-2.png" alt=""></button>
              <button type="button" class="app" data-act="app" data-name="Word" aria-label="Word"><img src="/assets/panel/app-3.png" alt=""></button>
              <button type="button" class="app" data-act="app" data-name="Notion" aria-label="Notion"><img src="/assets/panel/app-4.png" alt=""></button>
              <button type="button" class="app" data-act="app" data-name="Claude" aria-label="Claude"><img src="/assets/panel/app-5.png" alt=""></button>
              <button type="button" class="app" data-act="app" data-name="Acrobat" aria-label="Acrobat"><img src="/assets/panel/app-6.png" alt=""></button>
              <button type="button" class="app" data-act="app" data-name="WhatsApp" aria-label="WhatsApp"><img src="/assets/panel/app-7.png" alt=""></button>
              <button type="button" class="app" data-act="app" data-name="Xcode" aria-label="Xcode"><img src="/assets/panel/app-8.png" alt=""></button>
              <button type="button" class="app" data-act="app" data-name="Llama" aria-label="Llama"><img src="/assets/panel/app-9.png" alt=""></button>
            </div>
            <button type="button" class="power" data-act="quit" aria-label="Quit"><img src="/assets/panel/power.png" alt=""></button>
            <p class="panel-label shot-label">Screenshot</p>
            <p class="panel-label rec-label">Record</p>
            <div class="caps">
              <div class="cap-group" data-group="shot">
                <button type="button" class="shot" data-act="shot" data-kind="screen"><img src="/assets/panel/cap-0.png" alt=""><small>Screen</small></button>
                <button type="button" class="shot" data-act="shot" data-kind="area"><img src="/assets/panel/cap-1.png" alt=""><small>Area</small></button>
                <button type="button" class="shot" data-act="shot" data-kind="scroll"><img src="/assets/panel/cap-2.png" alt=""><small>Scroll</small></button>
              </div>
              <div class="cap-group" data-group="rec">
                <button type="button" class="shot" data-act="rec" data-kind="screen" aria-pressed="false"><img src="/assets/panel/cap-3.png" alt=""><small>Screen</small></button>
                <button type="button" class="shot" data-act="rec" data-kind="area" aria-pressed="false"><img src="/assets/panel/cap-4.png" alt=""><small>Area</small></button>
              </div>
            </div>
            <p class="panel-label tools-label">Tools</p>
            <div class="tools" data-group="tools">
              <button type="button" class="tool" data-act="focus" aria-pressed="false"><img src="/assets/panel/tool-0.png" alt=""><small>25 min</small></button>
              <button type="button" class="tool" data-act="shelf" aria-pressed="false"><img src="/assets/panel/tool-1.png" alt=""><small>Shelf</small></button>
              <button type="button" class="tool" data-act="copy"><img src="/assets/panel/tool-2.png" alt=""><small>Copy Text</small></button>
              <button type="button" class="tool" data-act="color"><img src="/assets/panel/tool-3.png" alt=""><small>Color</small></button>
              <button type="button" class="tool" data-act="qr"><img src="/assets/panel/tool-4.png" alt=""><small>Scan QR</small></button>
            </div>
            <p class="status" id="status" data-kind="shot"><svg class="check" viewBox="0 0 16 16" aria-hidden="true"><circle cx="8" cy="8" r="8" fill="currentColor"/><path d="M4.6 8.2 7 10.5 11.5 5.7" fill="none" stroke="#fff" stroke-width="1.7" stroke-linecap="round" stroke-linejoin="round"/></svg><span>Screenshot saved to Desktop</span><button type="button" data-act="finder">Show in Finder</button></p>
          </div>
        </div>
        <div class="desktop">
          <span class="demo-pointer" id="demo-pointer" hidden aria-hidden="true"></span>
          <p class="desktop-hint" id="glow-read">Bring the pointer near the notch.</p>
        </div>
      </div>
      <div class="stage-controls">
        <label class="switch"><input type="checkbox" id="fullscreen"> Full-screen app</label>
        <p>Preview only. This page does not capture your screen.</p>
      </div>
      <div class="keys" aria-label="Keyboard shortcuts">
        <span><kbd>Ctrl</kbd><kbd>Opt</kbd><kbd>Cmd</kbd><kbd>3</kbd> Screen</span>
        <span><kbd>Ctrl</kbd><kbd>Opt</kbd><kbd>Cmd</kbd><kbd>4</kbd> Area</span>
        <span><kbd>Ctrl</kbd><kbd>Opt</kbd><kbd>Cmd</kbd><kbd>7</kbd> Scroll</span>
        <span><kbd>Ctrl</kbd><kbd>Opt</kbd><kbd>Cmd</kbd><kbd>5</kbd> Record</span>
        <span><kbd>Ctrl</kbd><kbd>Opt</kbd><kbd>Cmd</kbd><kbd>6</kbd> Record area</span>
      </div>
    </div>
  </section>

  <section class="band" id="glow">
    <div class="frame">
      <p class="eyebrow">Glow</p>
      <h2>A light that knows how close you are.</h2>
      <p class="lede">Move toward the notch and a soft light appears around it. It gets brighter the closer the pointer gets. It pulses amber when something needs approval, and green when that thing is done.</p>
      <div class="grid-3">
        <article class="card"><p class="tag">Near</p><h3>Soft, then brighter</h3><p>The glow is faint at a distance and stronger as the pointer arrives. You can see Notchy notice you before the panel opens.</p></article>
        <article class="card"><p class="tag">Amber</p><h3>Needs approval</h3><p>The light pulses amber when something is waiting on you. A capture the Mac still has to allow is that kind of moment.</p></article>
        <article class="card"><p class="tag">Green</p><h3>Done</h3><p>The light pulses green when the thing finishes. A screenshot that has been saved is one of those.</p></article>
      </div>
    </div>
  </section>

  <section class="band alt" id="panel-feature">
    <div class="frame">
      <p class="eyebrow">Panel</p>
      <h2>Rest on the notch, or click it.</h2>
      <p class="lede">The panel drops down from the notch. Your shortcuts are on top. Screenshots, recording and tools are under them. Settings and Quit are at the corners.</p>
      <div class="grid-3">
        <article class="card"><h3>Shortcuts</h3><p>The top row is the apps you chose. Finder, Safari and Terminal are the ones that start there.</p></article>
        <article class="card"><h3>Screenshot and record</h3><p>The whole screen, an area, or a long scrolling page. Record the screen or an area, with a timer and Stop.</p></article>
        <article class="card"><h3>Settings and Quit</h3><p>Settings holds the shortcuts and the optional tools. Quit leaves Notchy.</p></article>
      </div>
    </div>
  </section>

  <section class="band" id="screenshots">
    <div class="frame">
      <p class="eyebrow">Screenshot</p>
      <h2>Three ways to grab the screen.</h2>
      <div class="grid-3">
        <article class="card"><p class="tag">Ctrl Opt Cmd 3</p><h3>Screen</h3><p>The whole screen, from the panel or from the keys.</p></article>
        <article class="card"><p class="tag">Ctrl Opt Cmd 4</p><h3>Area</h3><p>The part of the screen you choose.</p></article>
        <article class="card"><p class="tag">Ctrl Opt Cmd 7</p><h3>Scroll</h3><p>A long page that does not fit in one view.</p></article>
      </div>
      <p class="lede">When the shot is done, the glow pulses green. The panel can say it was saved to the Desktop.</p>
    </div>
  </section>

  <section class="band alt" id="record">
    <div class="frame">
      <p class="eyebrow">Record</p>
      <h2>A timer, and Stop.</h2>
      <div class="grid-2">
        <article class="card"><p class="tag">Ctrl Opt Cmd 5</p><h3>The whole screen</h3><p>Starts a recording of the screen. The same shortcut stops it. The panel shows the time and a Stop control.</p></article>
        <article class="card"><p class="tag">Ctrl Opt Cmd 6</p><h3>An area</h3><p>Starts a recording of the area you choose, and stops it again. The amber pulse is the “needs approval” light.</p></article>
      </div>
    </div>
  </section>

  <section class="band" id="tools">
    <div class="frame">
      <p class="eyebrow">Tools</p>
      <h2>The things you reach for.</h2>
      <div class="grid-3">
        <article class="card"><h3>Focus timer</h3><p>Starts at 25 minutes and counts down in the panel.</p></article>
        <article class="card"><h3>Drop shelf</h3><p>A place to leave something for a moment.</p></article>
        <article class="card"><h3>Copy text</h3><p>Reads type that is on the screen.</p></article>
        <article class="card"><h3>Scan QR</h3><p>Reads a code that is on the screen.</p></article>
        <article class="card"><h3>Color picker</h3><p>Reads the color under the pointer.</p></article>
        <article class="card"><h3>Keep awake</h3><p>Keeps the Mac from sleeping.</p></article>
        <article class="card"><h3>World clock</h3><p>Times in other places, from the same panel.</p></article>
        <article class="card"><h3>Camera mirror</h3><p>Optional. It uses the camera only if you turn it on.</p></article>
        <article class="card"><h3>Downloads and meetings</h3><p>Optional alerts for Downloads, and the next meeting. Both stay off until you want them.</p></article>
      </div>
    </div>
  </section>

  <section class="band alt" id="shortcuts">
    <div class="frame">
      <p class="eyebrow">Shortcuts</p>
      <h2>The same jobs, from the keyboard.</h2>
      <table class="spec">
        <thead><tr><th>Do this</th><th>Keys</th></tr></thead>
        <tbody>
          <tr><td>Screenshot the screen</td><td><kbd>Ctrl</kbd><kbd>Opt</kbd><kbd>Cmd</kbd><kbd>3</kbd></td></tr>
          <tr><td>Screenshot an area</td><td><kbd>Ctrl</kbd><kbd>Opt</kbd><kbd>Cmd</kbd><kbd>4</kbd></td></tr>
          <tr><td>Screenshot a scrolling page</td><td><kbd>Ctrl</kbd><kbd>Opt</kbd><kbd>Cmd</kbd><kbd>7</kbd></td></tr>
          <tr><td>Record the screen, and stop</td><td><kbd>Ctrl</kbd><kbd>Opt</kbd><kbd>Cmd</kbd><kbd>5</kbd></td></tr>
          <tr><td>Record an area, and stop</td><td><kbd>Ctrl</kbd><kbd>Opt</kbd><kbd>Cmd</kbd><kbd>6</kbd></td></tr>
        </tbody>
      </table>
    </div>
  </section>

  <section class="band" id="full-screen">
    <div class="frame">
      <p class="eyebrow">Full-screen apps</p>
      <h2>The glow stays out of the way.</h2>
      <p class="lede">When an app is full screen, Notchy keeps the glow off so it does not cover that app's menus. Only a click opens the panel. The switch under the preview does the same thing on this page.</p>
    </div>
  </section>

  <section class="band alt" id="questions">
    <div class="frame">
      <p class="eyebrow">Questions</p>
      <h2>Straight answers.</h2>
      <p class="lede">Longer versions are on the <a href="/blog/">blog</a>.</p>
      <div class="qa">
        <details><summary>What is Notchy?</summary><p>A Mac app that turns the notch into shortcuts, screenshots, recording and tools.</p></details>
        <details><summary>How does the glow work?</summary><p>A soft light appears as the pointer gets near, and it gets brighter the closer it gets. Amber means something needs approval. Green means it is done.</p></details>
        <details><summary>How do I open the panel?</summary><p>Rest the pointer on the notch, or click it. In a full-screen app, only the click opens it.</p></details>
        <details><summary>What are the shortcuts?</summary><p>Control, Option and Command, with 3, 4 and 7 for screenshots, and 5 and 6 for recordings.</p></details>
        <details><summary>Does this website capture my screen?</summary><p>No. The notch on this page is a preview. It does not take a screenshot, record, or turn a camera on.</p></details>
        <details><summary>How do I get the Mac app?</summary><p>Write to <a href="mailto:hello@jabble.si">hello@jabble.si</a>. This site does not take payment.</p></details>
      </div>
    </div>
  </section>

  <section class="close-band">
    <div class="frame">
      <h2>It runs on your Mac.</h2>
      <p class="lede">Bring the pointer near the notch. The panel does the rest.</p>
      <a class="pill primary" href="{MAIL}">Get Notchy</a>
    </div>
  </section>
</main>
"""


def subnav(current=""):
    items = [("Blog", "/blog/", "blog")] + [
        ("The notch", "/blog/topic/the-notch/", "the-notch"),
        ("Capture", "/blog/topic/capture/", "capture"),
        ("Tools", "/blog/topic/tools/", "tools"),
        ("The app", "/blog/topic/the-app/", "the-app"),
    ]
    links = []
    for name, href, key in items:
        cur = ' aria-current="page"' if key == current else ""
        links.append(f'<a href="{href}"{cur}>{name}</a>')
    return f'<nav class="subnav" aria-label="Blog topics"><div class="subnav-inner">{"".join(links)}</div></nav>'


def share(path, title, end=False):
    klass = "share share-end" if end else "share"
    return f'''<div class="{klass}" data-share data-path="{esc(path)}" data-title="{esc(title)}">
  <span class="share-label">Share</span>
  <a class="share-btn" data-share-x href="https://x.com/intent/post" target="_blank" rel="noopener" aria-label="Share on X (opens in a new tab)">{icon('<path fill="currentColor" d="M18.9 1.2h3.7l-8 9.2L24 22.8h-7.4l-5.8-7.6-6.6 7.6H.5l8.6-9.8L0 1.2h7.6l5.2 6.9Zm-1.3 19.5h2L6.5 3.2H4.3Z"/>')}</a>
  <a class="share-btn" data-share-li href="https://www.linkedin.com/sharing/share-offsite/" target="_blank" rel="noopener" aria-label="Share on LinkedIn (opens in a new tab)">{icon('<path fill="currentColor" d="M4.98 3.5C4.98 4.88 3.88 6 2.5 6S0 4.88 0 3.5 1.12 1 2.5 1s2.48 1.12 2.48 2.5zM.5 8.5h4V24h-4V8.5zM8.5 8.5h3.8v2.1h.1c.5-1 1.8-2.1 3.8-2.1 4 0 4.8 2.6 4.8 6V24h-4v-7.7c0-1.8 0-4.1-2.5-4.1s-2.9 2-2.9 4V24h-4V8.5z"/>')}</a>
  <a class="share-btn" data-share-mail href="mailto:" aria-label="Share by email">{icon('<rect x="3" y="5" width="18" height="14" rx="2" fill="none" stroke="currentColor" stroke-width="1.8"/><path d="m4 7 8 6 8-6" fill="none" stroke="currentColor" stroke-width="1.8"/>')}</a>
  <button type="button" class="share-btn" data-share-copy aria-label="Copy link">{icon('<path d="M10 14a4 4 0 0 0 5.7 0l3-3a4 4 0 0 0-5.7-5.7l-1 1M14 10a4 4 0 0 0-5.7 0l-3 3a4 4 0 0 0 5.7 5.7l1-1" fill="none" stroke="currentColor" stroke-width="1.8" stroke-linecap="round"/>')}</button>
  <span class="share-done" data-share-done role="status"></span>
</div>'''


def card_thumb(post, kind):
    slug = post["slug"]
    return (
        f'<span class="{kind} is-thumb" aria-hidden="true">'
        f'<img class="thumb-light" src="/assets/blog/{slug}.jpg" alt="" width="1200" height="630">'
        f'<img class="thumb-dark" src="/assets/blog/{slug}-dark.jpg" alt="" width="1200" height="630">'
        f"</span>"
    )


def _thumb_font(weight, size):
    from PIL import ImageFont

    return ImageFont.truetype(f"/usr/share/fonts/truetype/macos/Inter-{weight}.ttf", size)


def _thumb_wash(dark):
    from PIL import Image

    w, h = 1200, 630
    base = (29, 29, 31) if dark else (248, 248, 246)
    tint = (16, 44, 82) if dark else (198, 224, 250)
    peak = 0.78 if dark else 0.42
    im = Image.new("RGB", (w, h))
    px = im.load()
    cx, cy, reach = 1320, -120, 1180.0
    for y in range(h):
        dy = (y - cy) * (y - cy)
        for x in range(w):
            d = ((x - cx) * (x - cx) + dy) ** 0.5
            t = max(0.0, 1 - d / reach)
            t = t * t * peak
            px[x, y] = tuple(int(base[i] * (1 - t) + tint[i] * t) for i in range(3))
    return im


def _thumb_lines(draw, text, font, max_w):
    words = text.split()
    lines, cur = [], ""
    for word in words:
        trial = word if not cur else f"{cur} {word}"
        if draw.textlength(trial, font=font) <= max_w:
            cur = trial
        else:
            if cur:
                lines.append(cur)
            cur = word
    if cur:
        lines.append(cur)
    return lines


def _thumb_title(draw, title):
    chosen = None
    for size in (78, 70, 62, 56, 50):
        font = _thumb_font("Bold", size)
        lines = _thumb_lines(draw, title, font, 740)
        chosen = (font, lines, size)
        if len(lines) <= 2:
            return chosen
    return chosen


def _draw_tracked(draw, xy, text, font, fill, tracking):
    x, y = xy
    for ch in text:
        draw.text((x, y), ch, font=font, fill=fill)
        x += draw.textlength(ch, font=font) + tracking


def _thumb_motif(draw, kind, color):
    if kind == "capture":
        draw.rounded_rectangle((1024, 176, 1340, 468), radius=36, outline=color, width=8)
        draw.line((1104, 248, 1104, 400), fill=color, width=6)
        draw.line((1104, 248, 1256, 248), fill=color, width=6)
        draw.line((1188, 320, 1288, 320), fill=color, width=6)
        draw.line((1188, 320, 1188, 400), fill=color, width=6)
    elif kind == "tools":
        cx, cy, r = 1124, 318, 236
        draw.arc((cx - r, cy - r, cx + r, cy + r), start=206, end=338, fill=color, width=8)
        draw.line((cx, cy, cx + 78, cy - 108), fill=color, width=8)
        draw.ellipse((cx - 16, cy - 16, cx + 16, cy + 16), outline=color, width=8)
    elif kind == "app":
        for i, y in enumerate((168, 252, 336)):
            draw.rounded_rectangle((1048, y, 1124, y + 64), radius=16, outline=color, width=6)
            draw.rounded_rectangle((1148, y, 1224, y + 64), radius=16, outline=color, width=6)
    else:
        draw.rounded_rectangle((1016, -36, 1248, 124), radius=52, outline=color, width=8)
        draw.ellipse((1092, 48, 1112, 68), outline=color, width=6)
        draw.ellipse((1152, 48, 1172, 68), outline=color, width=6)
        draw.arc((900, 80, 1360, 420), start=18, end=162, fill=color, width=8)


def render_thumbs():
    from PIL import Image, ImageDraw

    marks = {
        dark: Image.open(ROOT / "assets" / "icon" / f"{name}.png").convert("RGBA").resize((52, 52), Image.Resampling.LANCZOS)
        for dark, name in ((False, "light"), (True, "dark"))
    }

    out = ROOT / "assets" / "blog"
    out.mkdir(parents=True, exist_ok=True)
    washes = {False: _thumb_wash(False), True: _thumb_wash(True)}
    lock = _thumb_font("Medium", 26)
    topic_font = _thumb_font("SemiBold", 28)
    for post in POSTS:
        for dark, base in washes.items():
            im = base.copy()
            draw = ImageDraw.Draw(im)
            motif = (64, 112, 158) if dark else (154, 194, 224)
            _thumb_motif(draw, post["thumb"], motif)
            topic = (100, 181, 255) if dark else (0, 102, 214)
            title_fill = (245, 245, 247) if dark else (29, 29, 31)
            lock_fill = (174, 174, 178) if dark else (84, 84, 86)
            draw.text((86, 82), post["topic"], font=topic_font, fill=topic)
            font, lines, size = _thumb_title(draw, post["title"])
            y = 156
            for line in lines:
                _draw_tracked(draw, (84, y), line, font, title_fill, -size * 0.012)
                y += int(size * 1.02)
            mark_y = 468
            im.paste(marks[dark], (80, mark_y), marks[dark])
            label = "Notchy blog"
            bbox = draw.textbbox((0, 0), label, font=lock)
            th = bbox[3] - bbox[1]
            draw.text((144, mark_y + (52 - th) / 2 - bbox[1]), label, font=lock, fill=lock_fill)
            name = f'{post["slug"]}-dark.jpg' if dark else f'{post["slug"]}.jpg'
            im.save(out / name, quality=88, optimize=True)
    return len(POSTS) * 2


def blog_index():
    feature = POSTS[0]
    picks = [p for p in POSTS if p["slug"] in {"the-glow", "screenshots", "shortcuts"}]
    rest = [p for p in POSTS if p is not feature]
    pick_html = "".join(
        f'<li><a href="/blog/{p["slug"]}/"><span class="pick-label">{esc(p["topic"])}</span><span class="pick-title">{esc(p["title"])}</span></a></li>'
        for p in picks
    )
    cards = []
    for i, p in enumerate(rest):
        hidden = " data-more hidden" if i >= 6 else ""
        cards.append(
            f'<li{hidden}><a class="grid-card" href="/blog/{p["slug"]}/">'
            f"{card_thumb(p, 'grid-img')}"
            f'<span class="card-label">{esc(p["topic"])}</span><span class="grid-title">{esc(p["title"])}</span></a></li>'
        )
    more = '<p class="read-more"><button type="button" class="pill secondary" id="blog-more">Read more</button></p>' if len(rest) > 6 else ""
    body = f"""<main>
{subnav("blog")}
<div class="blog-home">
  <h1 class="blog-h1">Notchy blog: the notch, put to work</h1>
  <div class="blog-top">
    <a class="feature-card" href="/blog/{feature["slug"]}/">
      {card_thumb(feature, "feature-img")}
      <span class="feature-text"><span class="card-label">{esc(feature["topic"])}</span><span class="feature-title">{esc(feature["title"])}</span></span>
    </a>
    <section class="picks" aria-labelledby="picks-title">
      <h2 id="picks-title">{icon('<path d="M12 2.5l2.1 6.2 6.4 2.3-6.4 2.3L12 19.5l-2.1-6.2L3.5 11l6.4-2.3z" fill="currentColor"/>')}Good places to start</h2>
      <ul>{pick_html}</ul>
    </section>
  </div>
  <section aria-label="Every article"><ul class="blog-grid">{"".join(cards)}</ul>{more}</section>
</div>
</main>"""
    return shell("Notchy blog: the notch, put to work", "Guides for Notchy, the Mac app that lives in the notch: glow, screenshots, recording and tools.", body, blog=True, blog_current=True)


def post_page(post, nxt):
    toc = "".join(f'<li><a href="#{i}">{esc(h)}</a></li>' for i, h, _ in post["sections"])
    prose = "".join(f'<h2 id="{i}">{esc(h)}</h2>{body}' for i, h, body in post["sections"])
    related = ""
    if nxt:
        items = "".join(
            f'<li><a href="/blog/{p["slug"]}/"><span class="card-date">{esc(p["topic"])} · {p["minutes"]} min read</span><span class="card-title">{esc(p["title"])}</span><span class="card-desc">{esc(p["description"])}</span></a></li>'
            for p in nxt
        )
        related = f'<section class="related" aria-labelledby="related-title"><h2 id="related-title">Keep reading</h2><ul>{items}</ul></section>'
    next_link = ""
    if nxt:
        p = nxt[0]
        next_link = f'<p class="read-next"><a href="/blog/{p["slug"]}/"><span class="read-next-label">Next</span><span class="read-next-title">{esc(p["title"])}</span><span class="read-next-more">Keep reading · {p["minutes"]} min</span></a></p>'
    path = f'/blog/{post["slug"]}/'
    body = f"""<main>
{subnav(post["topic_slug"])}
<div class="post-grid">
  <aside class="toc-side"><nav class="toc" aria-label="On this page"><p class="toc-title">On this page</p><ol>{toc}</ol></nav></aside>
  <article class="post">
    <nav class="crumbs" aria-label="Breadcrumb"><ol><li><a href="/">Notchy</a></li><li><a href="/blog/">Blog</a></li><li><a href="/blog/topic/{post["topic_slug"]}/">{esc(post["topic"])}</a></li></ol></nav>
    <h1>{esc(post["title"])}</h1>
    <p class="byline">By Noaman, maker of Notchy · <time datetime="{post["date"]}">{pretty_date(post["date"])}</time> · {post["minutes"]} min read</p>
    {share(path, post["title"])}
    <aside class="quick-answer" aria-label="Quick answer"><p class="qa-label">Quick answer</p><p>{esc(post["quick"])}</p></aside>
    <details class="toc-inline"><summary>On this page</summary><ol>{toc}</ol></details>
    <div class="prose">{prose}
      <aside class="mid-cta"><p><b>Notchy lives in the notch.</b> Glow, panel, screenshot, record.</p><a class="pill primary" href="{MAIL}">Get Notchy</a></aside>
    </div>
    {share(path, post["title"], end=True)}
    {next_link}
    <p class="plain-copy">Also as <a href="/blog/{post["slug"]}.md">plain text</a>, for AI assistants and readers.</p>
    <aside class="end-cta"><p><b>Screenshot, record, focus.</b> All from the notch.</p><a class="pill primary" href="{MAIL}">Get Notchy</a></aside>
    {related}
  </article>
</div>
</main>"""
    return shell(f'{post["title"]} · Notchy blog', post["description"], body, blog=True, blog_current=True)


def markdown(post):
    import re
    lines = [f'# {post["title"]}', "", post["quick"], ""]
    for _, heading, body in post["sections"]:
        lines.append(f'## {heading}')
        text = body
        text = re.sub(r'<span class="vh">.*?</span>', "", text)
        text = re.sub(r'<a [^>]*href="([^"]+)"[^>]*>', r"\1 ", text)
        text = text.replace("</a>", "")
        text = text.replace("<ul>", "").replace("</ul>", "")
        text = text.replace("<li>", "- ").replace("</li>", "")
        text = text.replace("<p>", "").replace("</p>", "\n")
        text = text.replace("<kbd>", "").replace("</kbd>", " ")
        text = text.replace("<strong>", "").replace("</strong>", "")
        text = re.sub(r"[ \t]{2,}", " ", text)
        text = re.sub(r" *\n *", "\n", text)
        lines.append(text.strip())
        lines.append("")
    return "\n".join(lines)


def topic_page(slug, name, intro):
    posts = [p for p in POSTS if p["topic_slug"] == slug]
    cards = "".join(
        f'<li><a class="grid-card" href="/blog/{p["slug"]}/"><span class="card-date">{pretty_date(p["date"])} · {p["minutes"]} min</span><span class="card-title">{esc(p["title"])}</span><span class="card-desc">{esc(p["description"])}</span></a></li>'
        for p in posts
    )
    body = f"""<main>
{subnav(slug)}
<div class="topic-page">
  <p class="eyebrow">{esc(name)}</p>
  <h1>{esc(name)}</h1>
  <p class="lede">{esc(intro)}</p>
  <ul class="cards">{cards}</ul>
</div>
</main>"""
    return shell(f'{name} · Notchy blog', intro, body, blog=True, blog_current=True)


def doc(title, paragraphs):
    ps = "".join(f"<p>{p}</p>" for p in paragraphs)
    body = f'<main><article class="doc"><div class="frame"><div class="narrow"><p class="eyebrow">Notchy</p><h1>{esc(title)}</h1>{ps}<p><a href="/">Back to Notchy</a></p></div></div></article></main>'
    return shell(f'{title} · Notchy', paragraphs[0][:150], body)


def rss():
    items = []
    for p in sorted(POSTS, key=lambda x: x["date"], reverse=True):
        pub = datetime.strptime(p["date"], "%Y-%m-%d").strftime("%a, %d %b %Y 00:00:00 +0000")
        items.append(
            f'<item><title>{esc(p["title"])}</title><link>/blog/{p["slug"]}/</link>'
            f'<guid>/blog/{p["slug"]}/</guid><pubDate>{pub}</pubDate><description>{esc(p["description"])}</description></item>'
        )
    return f'''<?xml version="1.0" encoding="UTF-8"?>
<rss version="2.0"><channel>
<title>Notchy blog</title>
<link>/blog/</link>
<description>Guides for Notchy, the Mac app that lives in the notch.</description>
{"".join(items)}
</channel></rss>
'''


def main():
    print("thumbs", render_thumbs())
    write("index.html", shell(
        "Notchy for Mac · Screenshot, record, focus, from the notch",
        "Notchy turns the notch on your Mac into shortcuts, screenshots, screen recording and tools. The glow brightens as the pointer gets close.",
        HOME,
    ))
    write("blog/index.html", blog_index())
    write("blog/rss.xml", rss())
    for i, post in enumerate(POSTS):
        nxt = [POSTS[(i + 1 + n) % len(POSTS)] for n in range(3) if POSTS[(i + 1 + n) % len(POSTS)] is not post]
        # next 3 forward, not wrapping onto itself only
        nxt = []
        for n in range(1, 4):
            nxt.append(POSTS[(i + n) % len(POSTS)])
        write(f'blog/{post["slug"]}/index.html', post_page(post, nxt))
        write(f'blog/{post["slug"]}.md', markdown(post))
    topics = {
        "the-notch": ("The notch", "How the glow and the panel work, and how that differs from a music notch."),
        "capture": ("Capture", "Screenshots, recording, the keyboard shortcuts, and the keys the Mac already has."),
        "tools": ("Tools", "Focus timer, shelf, copy text, Scan QR, color, and the optional tools."),
        "the-app": ("The app", "Full-screen apps, where a screenshot is saved, and the other apps in the notch."),
    }
    for slug, (name, intro) in topics.items():
        write(f"blog/topic/{slug}/index.html", topic_page(slug, name, intro))
    write("privacy.html", doc("Privacy", [
        "This website does not ask you to sign in, and it does not run analytics.",
        "The notch on the home page is a preview. It does not take a screenshot, record the screen, read pixels, watch a Downloads folder, read a calendar, or turn a camera on.",
        'Email to <a href="mailto:hello@jabble.si">hello@jabble.si</a> is the message you wrote. The site does not add a form or a tracker.',
        "On the Mac, a finished screenshot can be saved to the Desktop. This site has no library of those files.",
    ]))
    write("terms.html", doc("Terms", [
        "This site describes Notchy, a Mac app from Jabble Super Intelligence Inc. The preview on the home page is an explanation. It is not the app.",
        'There is no checkout on this site. Writing to <a href="mailto:hello@jabble.si">hello@jabble.si</a> asks about the Mac app. It does not buy a license.',
        "Apple, Mac, macOS and Finder are trademarks of Apple Inc. Notchy isn't made or endorsed by Apple.",
    ]))
    write("license.html", doc("License", [
        "A license for the Mac app is not sold on this website.",
        "Email <a href=\"mailto:hello@jabble.si\">hello@jabble.si</a> and we'll say how to try Notchy.",
    ]))
    write("refunds.html", doc("Refunds", [
        "This site does not take payment, so there is nothing to refund.",
    ]))
    write("your-data.html", doc("Your data", [
        'This website does not have accounts. Loading a page does not create a Notchy profile. The only message we receive is an email you send yourself to <a href="mailto:hello@jabble.si">hello@jabble.si</a>.',
        "The preview does not capture your screen. On the Mac, the panel can report a screenshot saved to the Desktop. This site does not upload that file.",
    ]))
    print("wrote", len(list(ROOT.glob("**/*.html"))), "html files")


if __name__ == "__main__":
    main()
