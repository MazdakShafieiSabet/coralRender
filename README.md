# coralRender
A Python tool for batch rendering Blender Files.

# Features
- **Render out files after one another:** got multiple files you need to render overnight? Just hit render, and watch it go. Or well, don't. Head to bed.
- **File Output Node only:** If you have one or more File Output Nodes in the Compositor and want to only use those to export your Multi-Layer EXRs, you don't have to manually delete the excess double exports manually. coralRender takes care of it.
- **Faster render times**: yes, you read that right. Your eyes did not deceive you. You will get a small (and I really mean small) performance boost because coralRender renders in the CLI leading to no overhead from the Blender UI. Though, you do have to have your scene fully prepped.

# Blender prepping
This section shows how to install Blender and how to set it up properly to use with coralRender.

Firstly
