[link.ug_samp_shots]
[wrap_h.chapter(t="##Sample A/V Script using *avshot* builtin")]

In this example, we will review an actual AV script from a project I did a few years back. This version was originally written using the old **avscript** version of the software, before it supported embedding images, so it's entirely done using text to describe the visuals and narration. It was converted to conform to the new [smd.b] builtins for inclusion in the user guide.

@import "[sys.imports]/divs.md"

// Include the **avshot** builtin to get the support for easily formatting AV Scripts
@import "[sys.imports]/avs/avs.md"

// Include the avs/shotacro.md builtins file to get various shot shorthand variable declarations
@import "[sys.imports]/avs/shotacro.md"

{:.center.blue}# AAT 4th Gen Video Series

@link _="me" _inherit="_template_" _text="me" href="email@yourdomain.com"
@link _="feedback" _inherit="me" _text="feedback" href="DELETE_ME_mailto:email@yourdomain.com?subject=Your%20Film%20Title%20Feedback"

[var.cover(title="Using iOS Devices with the AAT" author="Ken Lowrie" logline="This video shows how to use iOS devices to connect to the AAT's internal web server to control and manage the AAT. This video demonstration will use an iPhone and iOS 8.3.")]
[var.revision.plain(v="1a")]
[var.contact(cn="Ken Lowrie" ph="407-555-1000" em="[me]" c1="Copyright (c) 2015 by Sunsight Instruments." c2="All Rights Reserved." c3="Antenna Alignment Tool")]
[var.review.wc_open(t="Notes to Reviewers")]
    Please send feedback by marking up the PDF using embedded comments or notes. If you edit the PDF text directly, be sure to change your font color so that I can easily find the changes.

    Notes that begin with [spanwc.<(class="blue")]"VOICEOVER NOTE"[spanwc.>] or [vo.inline(t="are inside a box like this")]
    can be ignored; they are for the voiceover guy.

    Additions ++are now marked like this++ and deletions ~~are now marked like this~~

    Thanks in advance for reviewing and commenting on the script!
[var.review.wc_close]

[section(t="Script begins here")]

[avshot.visual]
    [cgi]Using iOS devices with the AAT
    *RECAP*: Show clips from finished video timelines that recap
    [cgi]iPhone or iPad Devices can operate the AAT
    [cgi]iOS v7.1.2 or later required
[avshot.audio]
    Welcome to *Using iOS devices with the AAT*. 

    In this video, we will show you how to control your AAT using an iOS device. It's simple and efficient, using tools that you are already familiar with: Your iOS Device and a Web Browser! Here's a quick preview:

    First, power on the AAT and wait for AZM to begin flashing
    Then, connect to the AAT hotspot with your iOS device
    Finally, open aat.sunsight.com in your browser, or just touch the AAT home page icon

    And that's all there is to it! 

    Once you've connected, you can do things like print site reports, email those reports to your customers, and more.

    Using iOS devices to connect to the AAT's internal web server allows you to access the User Interface or UI, which in turn, enables you to fully manage and/or control the AAT.  
[avshot.end]

// Here is a good example of when @break or @exit will be needed. If you don't clear the floats, then the browser attempts to fill in the space between them and below the visual with everything that follows, until you get past the entire shot...
@break

[avshot.visual]
    Additional setup and shortcuts are covered
    Adobe Acrobat Reader for viewing PDF reports
    How to create a PDF Report
    Sending PDF reports to your customers
[avshot.audio]
    ++In the remainder of this video, we will cover a one-time setup for your iOS device that enables you to efficiently control your AAT.++

    We will cover how to set up a home screen shortcut, to make accessing the AAT quick and easy, and we'll discuss Adobe's Acrobat Reader application for viewing PDF reports on your device. 

    After a quick introduction on generating PDF reports, we'll show you how to get the PDF reports to your customers.
[avshot.end]

[avshot.visual]
    Requirements and Limitations
    The AAT should be powered on and ready for clients to attach
    Refer to ***Connecting to the AAT with the Android Phone*** for details
    Only one (1) user can be connected at a time
[avshot.audio]
    This video assumes the AAT is powered on and ready for clients to attach to its internal hotspot. View the video entitled ***Connecting to the AAT with the Android Phone*** to learn about the AAT startup process.

    Keep in mind that only one user can control the AAT through its onboard website at a time. Multiple users connected at the same time is not supported.
[avshot.end]

[avshot.visual]
    SIDEBAR: Connecting to the AAT's Wireless Network
    IMAGE: Picture of an iPhone or an iPad
    Connecting to the network will look different depending on your hardware and software
    Process is *identical* to connecting to *any* wireless hotspot
    Refer to your device documentation for additional help
[avshot.audio]
    ++You'll need an iOS device that is running version 7.1.2 or later in order to use it to control the AAT.++

    In the demonstration, we will be using an iPhone 6+ running iOS 8.3 with the native Safari browser. You can use other iOS browsers, such as Google Chrome, if you prefer.

    Depending on the hardware and software version of your iOS device, along with the browser you are using, this process may look slightly different than what is shown in the video.

    The good news is that connecting to the AAT's wireless network is ***identical*** to connecting to any wireless hotspot, so if you are having trouble figuring out how to do this, refer to the documentation that came with your iOS device for additional assistance. 

    Let's go ahead and watch the demonstration of using an iOS device to control the AAT. The first step is to connect to the AAT's Wireless Network or hotspot. 
[avshot.end]

[avshot.visual]
    SCAST: Show AAT WiFi Network Connect via iOS 8.3
[avshot.audio]
    To do this, on your iOS device, choose SETTINGS, and then select Wi-Fi. 

    Ensure Wi-Fi is on, and then look for the AAT Wireless hotspot. 

    The AAT hotspot has a network name beginning with *AAT 90*, followed by a series of digits that represent the serial number of the unit. The serial number is on a printed decal affixed to the back of the tool.

    Touch the AAT hotspot in the list to initiate the connection. 

    You can tell that you have successfully connected to the hotspot when the name appears with a checkmark next to it, *and* the WiFi icon is displayed in the top left status bar, as shown in the video.
[avshot.end]
@break

[avshot.visual]
Connecting to the AAT
SCAST: Show the iOS home screen display and dock, and touch the Safari icon
[avshot.audio]
    Now that we are connected to the AAT hotspot, we are ready to access the AAT User Interface. To do that, you need to launch Safari, so go ahead and find the *Safari* icon on your iOS Device, normally located on the dock, and touch it to launch the browser.
[avshot.end]

[avshot.visual]
    Launch the AAT User Interface
    SCAST: Touch the new tab icon in Safari
    SCAST: Show aat.sunsight.com and then Home page
    SCAST: Show 192.168.0.50 and then Home page
[avshot.audio]
    [vo.nd(t="GREGG: BEWARE!!![bb]Here is that AAT dot SUNSIGHT dot COM again... :)")]

    To start the User Interface, open an empty browser tab, and in the address field, enter the URL *aat.sunsight.com*, and then press *GO*. The AAT user interface home page will be displayed, and you're now ready to setup, manage profiles and print reports!

    Alternatively, you can enter the IP address of the AAT, which is usually, 192.168.0.50.  Enter it ***exactly*** as shown, with the periods separating the four groups of digits. Press the GO key and wait for the home page of the AAT user interface to display. 
[avshot.end]

[avshot.visual]
Optional Step - Saving a shortcut or bookmark
Save a shortcut on the home screen to quickly return to the AAT home page
[avshot.audio]
    To save time starting the AAT User Interface in the future, you can create a shortcut on your home screen, which you can then tap to go directly to the AAT home page. 
[avshot.end]

[avshot.visual]
SCAST: Show the sharing icon and save to home screen
SCAST: Show launching AAT UI via home screen icon
[avshot.audio]
    To add a shortcut to the home screen, start Safari and launch the AAT User Interface by typing *aat.sunsight.com* in the address bar, and then touch the sharing icon (located at the bottom of the page on an iPhone, or at the top next to the address bar on an iPad). 

    Choose *Add to Home Screen*, and type in a name, such as *AAT*, press the *ADD button*, and the shortcut will be added to your homescreen. 

    From now on, after connecting to the AAT's WiFi network, you can simply touch the shortcut icon on the home screen to start the AAT User Interface, instead of launching the browser and typing in the URL or IP Address!
[avshot.end]

[avshot.visual]
SCAST: Show the sharing icon and add bookmark icon
SCAST: Show launching AAT UI via browser bookmark
[avshot.audio]
    In addition to saving a shortcut on the home screen, you can create a bookmark by tapping the Bookmark icon, also available on the sharing submenu. 

    Enter the name you'd like to use, then touch *Save*. 

    To access the bookmark later, simply tap the bookmark icon from inside the browser, and then tap on the saved AAT Bookmark.
[avshot.end]

[avshot.visual]
    Adobe Acrobat
    Allows viewing and managing PDF reports
    Provides a means of saving PDF reports so they can be recalled later
    This app is optional; it is not needed to view or email PDFs on iOS
[avshot.audio]
    You can install the free Adobe Acrobat application from the App store in order to view and manage AAT reports in PDF format on your iOS device. 

    PDF format is a very convenient way to send reports generated by the AAT to your customers, usually via email. In addition, the Adobe Acrobat app provides a convenient way to save reports and email them later.

    Keep in mind that installing the Adobe Acrobat application is optional, and is not needed to view or email PDF reports on your iOS device.
[avshot.end]

[avshot.visual]
    SCAST: Show how to download/install Adobe Acrobat via the App store
[avshot.audio]
    To install Adobe Acrobat, start the *App Store* by touching the *App Store icon* on the home screen.

    Press the *Search button* in the bottom bar, and then, in the search area, type *ADOBE ACROBAT* to locate the free download, and then install the application on your device.

    [note.nd(t="**NOTE**: Your device must be configured with an account in order to access the App Store. Refer to the documentation that came with your device for further information.")]
[avshot.end]
@break

[avshot.visual]
Generating Reports
Site Reports can be generated in Adobe PDF format
View reports before sharing to verify data is complete and accurate
[avshot.audio]
    Once you have completed your work using the AAT, you can generate site reports in Adobe PDF format to send to your customers.
[avshot.end]

[avshot.visual]
    SCAST: Show the site report being generated
[avshot.audio]
    To generate the PDF site report, touch the "Profiles, Captures, Reports" tab on the AAT Website, and then touch the PDF button next to the site you want to report on, or select "All PDF" to report on all sites.

    The PDF report is generated and shown in the browser tab, at which point you can review the report, then when you're ready, press the SHARE icon, and choose your preferred method for sharing with your customer.
[avshot.end]

[avshot.visual]
    SCAST: Show opening the PDF in Adobe Reader app
[avshot.audio]
    If you have an optional PDF Viewer installed on your iOS device, such as the free Adobe Acrobat app, you can use the *Open in* feature of iOS to view your report and store it. 

    Once you open a report in the Adobe Acrobat app, it is saved there, and can be reviewed and shared at a later time. 

    This provides a convenient way to access your reports without needing to reconnect to the AAT, and regenerate them.
[avshot.end]

[avshot.visual]
    Sharing Reports
    To email reports, you must have an email account configured on your iOS device
    Refer to your iOS documentation or consult your IT department for assistance
[avshot.audio]
    In most cases, you'll want to email the generated PDF reports to your customers. 

    In order to do this, an email account must be configured on your iOS device, and you must be connected to the Internet, either via a mobile data connection, or via a wireless connection with Internet connectivity. 

    Refer to the iOS documentation if you need assistance with configuring an email account on your device, or consult with your company's IT staff..

    [note.nd(t="**REMEMBER**: The AAT's internal wireless hotspot does *not* have Internet connectivity. While attached to the AAT, however, you can generate and *share* the PDFs via email, they just won't be sent until the device is connected to the Internet.")]

[avshot.end]

[avshot.visual]
    SCAST: Email report to customer
[avshot.audio]
    To email the report to a customer, touch the *Sharing* icon, and then touch the *mail* icon. Compose your email and press the *SEND* button to finish. You may wish to verify that the email with the report was sent successfully.
[avshot.end]

[avshot.visual]
Summary
[avshot.audio]
    This concludes the video on using iOS devices for operating and managing the AAT. 

    We've seen how to connect to the AAT's built-in WiFi hotspot and launch the AAT User Interface, as well as how to create shortcuts for quickly navigating to the AAT's web site. 

    We also discussed using the Adobe Acrobat application for viewing and managing PDFs. 

    Finally, we learned how to generate a site report and email it to a customer.

    If you need information on connecting to the AAT using Windows or Android Devices, refer to the specific training videos available on the training page at sunsight.com. Thanks for watching!
[avshot.end]

[section(t="Shotlist, Images and Screen Captures for Video")]

