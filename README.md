Assets Browser
==============

Tool to browse and access game assets.


To Run
======

```
chmod 755 assetsbrowser.py
./assetsbrowser.py
```

Screenshots
===========

![Main Window1](https://github.com/igormorgado/assetsbrowser/blob/master/screenshots/mainwindow1.png)

![Main Window2](https://github.com/igormorgado/assetsbrowser/blob/master/screenshots/mainwindow2.png)

![Texture Detail](https://github.com/igormorgado/assetsbrowser/blob/master/screenshots/assetview.png)

![About](https://github.com/igormorgado/assetsbrowser/blob/master/screenshots/about.png)


TO DO
=====

In Assets_Browser_Window:

1. Why Open button is pressed?
2. Why Repository Properties (eye) is pressed?
3. Why Search bar is away from Pull down options?
4. Why Open Recent pulldown button is large?
5. On Search pull down is there a better widget to do the same operations in Type and Size? (for size maybe use a ComboMenu 16 32 64 128 256 512 1024 2048 4096  plus empty option
6. Add perspective pickups to search as:
Axonometric: Iso Metric, Dimetric, Trimetric,
Orthogonal, Projective.
Side scroll, topdown

Adding new path will create new repository for each asset tupe

Asset types are:
  Textures (Textures, Tiles, SkyMaps)
  Audio (Sound effects, ambient music)

7. Create Repository properties window
8. Add "favorites"  icon over favorites textures, display only favorites too in search bar

Zooming
Thumbnail
Sort order (name, size, type, date)
Show more info in browser screen as (size,  type, name)
Add toggle view (list/flowbox)
Many source paths

On texture_window:

1. Do not stretch the selected flowbox verticaly. 
2. Window minimum height is the size of ate least one texture + datainfo height
3. How to remove bottom internal border from asset_friendly_name (to put them tighter with the "subtitle"
4. How to reduce the size of subtitle,based on title size?
5. How to make Title text bold.
6. An OpenGL view to display textures with applied shaders.

