# coralRender
A Python tool for batch rendering Blender Files.

# Features
- **Render out files after one another:** got multiple files you need to render overnight? Just hit render, and watch it go. Or well, don't. Head to bed.
- **File Output Node only:** if you have one or more File Output Nodes in the Compositor and want to only use those to export your Multi-Layer EXRs, you don't have to manually delete the excess double exports manually. coralRender takes care of it.
- **Faster render times**: yes, you read that right. Your eyes did not deceive you. You will get a small (and I really mean small) performance boost because coralRender renders in the CLI leading to no overhead from the Blender UI. Though, you do have to have your scene fully prepped.

# Prepping Blender
This section shows how to install Blender and how to set it up properly to use with coralRender.

Firstly, grab the newest stable version of Blender and install it. 

**Windows**
<br>
If you're on Windows go to the Blender homepage and click download. After that use the .msi or .msix file to install Blender. Note where it's being installed. If you already have it installed and you forgot where it is, it's typically installed in "C:\Program Files\Blender Foundation\Blender xx\" where xx in this context is the version number. Then hit the Windows-logo on your keyboard and search for "Environment". The search result you're looking for is called "Edit the system environment variables". Hit enter and look for the button "Environment Variables...". Click it and it'll take you to the page that lets you add a path to PATH (pun intended) Under "User Variables" find "Path", double-click it and select new. Now paste in the Blender install path you definitely copied. Press enter and close out of all of this. Now if you open a termial and type
```
blender -v
```
You should see an output. If you scroll a bit up to where the output begins, you see your Blender version. Yay, you added Blender to PATH!

**Linux**
<br>
On Linux I recommend using the Flatpack or the Snap package as those (in my experience) default to shipping with OPTIX. You may also use the build coming in your package manager or even build one from source, I just recommend a different way. Anyway, Linux makes it easy on us since you do not need to add anything to PATH. Yay, you're basically done. And that kids, is why Linux is objectively better.

**macOS**
<br>
Unfortunately, macOS is not currently a priority with this tool and it's a system I do not know well enough to develop for. It is in the future roadmap to add extensive Mac support. And if you're thinking "It's just a Python script, it cannot be that serious", I would have thought the same. But I have been dissapointed so often when trying to write and it works on Windows and Linux, but my friends can't run it cuz it's on a Mac. Right now the focus is to get a stable, working little app. That's all.
