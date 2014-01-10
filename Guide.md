Update guide
============

1.  Open `pacgen_report.html`
2.  Look for new mod to install
3.  Control click (or middle click) the update button this will take you to the
    mods page, now download the newest file from here open up admin files and click
    on *select files* under *Single Upload*. Navigate to where the download file has been
    saved and upload that.
4.  When it's finished uploading a pop up will come up showing the new XML info.
    Leave that open and go over to the *admin XML* tab.
5.  Find the mod you have updated in the XML and copy over what's in the small box
    (on the admn files tab) and replace the old info with the new info (on the
    *admin XML* tab)
6.  Click *save*.
7.  Restart the launcher and launch your dev version of RW. Make sure you get to the main
    screen and it's not crashing, if it does crash you'll need to find the problem.

IF IT CRASHES
-------------

1.  Open up the launcher and click on open folder under RW's instances.
2.  Find a folder called `ForgeModLoader-0.log` and open it with
    your favourite text editor (for example *notepad++*)
3.  From here click on the search tab at the top of the page.
    Type in conflict and press in current document.
    This should bring up any conflicts there is.
    From here you need to edit the config file of the mod to an ID that's free
    (this includes **Items ID'**s too, **Item ID**'s are offset by 265 meaning if it
    says the **Item ID** is *26000* on the notepad the **Physical ID** in game
    is *26256*,
    keep this in mind when trying to find free **Item ID**'s using the pack dumps we have
4.  Once conflicts have been sorted load MC and make sure it gets to the main screen,
    check the `ForgeModLoader-0.log` for any other conflicts (you can get
    **Item ID** conflicts.
    even if the main screen loads up!)
5.  If you have changed any configs at all you'll need to also save them to the git
    repository folder under the configs folder. **IMPORTANT**, otherwise people aren't
    going to get your changes.
6.  Also if you have added a mod and there wasn't any config issue whatsoever,
    you still need to update the configs in git hub as above, this is so anything
    new added will get saved for the rest of us too.

IF THE ABOVE IS FINE OR YOU HAVE DONE THE CHANGES CARRY ON
----------------------------------------------------------

1.  Now that everything is ok and MC runs fine with no conflicts or issues copy over
    the new mod info to the pack.xml, this will change things for other people.
2.  Once you have done that save the new info and commit the changes, then push.
3.  Rinse and repeat
