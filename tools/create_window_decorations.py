#!/usr/bin/env python3
"""
Generate Window Decorations (Metacity-1) and GTK 3.0 / GTK 4.0 Theme:
Windows 11 Frosted Acrylic Glass with Stark Cyan and Hot-Rod Red Accents.
"""

import os

THEME_ROOT = "/home/MR_Gray/muteX/theme"
META_DIR = os.path.join(THEME_ROOT, "metacity-1")
GTK3_DIR = os.path.join(THEME_ROOT, "gtk-3.0")
GTK4_DIR = os.path.join(THEME_ROOT, "gtk-4.0")

os.makedirs(META_DIR, exist_ok=True)
os.makedirs(os.path.join(GTK3_DIR, "assets"), exist_ok=True)
os.makedirs(os.path.join(GTK4_DIR, "assets"), exist_ok=True)

# 1. Metacity theme descriptor metacity-theme-3.xml
metacity_xml = """<?xml version="1.0"?>
<metacity_theme>
<info>
  <name>Jarvis-Windows11-Shell</name>
  <author>Tony Stark / MR_Gray</author>
  <copyright>GPL</copyright>
  <date>2026</date>
  <description>Stark Industries Windows 11 frosted acrylic window decoration theme with glowing cyan and red controls.</description>
</info>

<!-- ::: CONSTANTS ::: -->
<constant name="C_title_focused" value="#F0F6FC" />
<constant name="C_title_unfocused" value="#64748B" />

<constant name="C_wm_bg" value="#080E18" />
<constant name="C_wm_bg_unfocused" value="#0A101C" />

<constant name="C_wm_border" value="#00E5FF" />
<constant name="C_wm_border_unfocused" value="#1E293B" />
<constant name="C_wm_highlight" value="#0D1829" />

<!-- Window Button Colors (Windows 11 Style with Stark Highlights) -->
<constant name="C_btn_close_bg_hover" value="#E81123" />
<constant name="C_btn_close_fg" value="#FFFFFF" />

<constant name="C_btn_bg_hover" value="#1E293B" />
<constant name="C_btn_fg" value="#00E5FF" />
<constant name="C_btn_fg_unfocused" value="#64748B" />

<!-- ::: GEOMETRY ::: -->
<frame_geometry name="normal" title_scale="medium" rounded_top_left="10" rounded_top_right="10">
  <distance name="left_width" value="1" />
  <distance name="right_width" value="1" />
  <distance name="bottom_height" value="1" />
  <distance name="left_titlebar_edge" value="8" />
  <distance name="right_titlebar_edge" value="8" />
  <distance name="top_titlebar_edge" value="2" />
  <distance name="bottom_titlebar_edge" value="2" />
  <distance name="title_vertical_pad" value="8" />
  <border name="title_border" left="6" right="6" top="2" bottom="2" />
  <border name="button_border" left="4" right="4" top="4" bottom="4" />
</frame_geometry>

<frame_geometry name="maximized" parent="normal" rounded_top_left="0" rounded_top_right="0">
  <distance name="left_width" value="0" />
  <distance name="right_width" value="0" />
  <distance name="bottom_height" value="0" />
</frame_geometry>

<!-- ::: DRAW OPS ::: -->
<draw_ops name="draw_frame_focused">
  <rectangle color="C_wm_bg" x="0" y="0" width="width" height="height" filled="true" />
  <line color="C_wm_border" x1="0" y1="height - 1" x2="width" y2="height - 1" width="1" />
  <line color="C_wm_border" x1="0" y1="0" x2="width" y2="0" width="1" />
</draw_ops>

<draw_ops name="draw_frame_unfocused">
  <rectangle color="C_wm_bg_unfocused" x="0" y="0" width="width" height="height" filled="true" />
  <line color="C_wm_border_unfocused" x1="0" y1="height - 1" x2="width" y2="height - 1" width="1" />
</draw_ops>

<!-- Close Button -->
<draw_ops name="btn_close_normal">
  <line color="C_btn_fg" x1="4" y1="4" x2="12" y2="12" width="1.5" />
  <line color="C_btn_fg" x1="12" y1="4" x2="4" y2="12" width="1.5" />
</draw_ops>

<draw_ops name="btn_close_hover">
  <rectangle color="C_btn_close_bg_hover" x="0" y="0" width="width" height="height" filled="true" />
  <line color="#FFFFFF" x1="4" y1="4" x2="12" y2="12" width="1.8" />
  <line color="#FFFFFF" x1="12" y1="4" x2="4" y2="12" width="1.8" />
</draw_ops>

<!-- Maximize Button -->
<draw_ops name="btn_max_normal">
  <rectangle color="C_btn_fg" x="3" y="3" width="10" height="10" filled="false" />
</draw_ops>

<draw_ops name="btn_max_hover">
  <rectangle color="C_btn_bg_hover" x="0" y="0" width="width" height="height" filled="true" />
  <rectangle color="#FFFFFF" x="3" y="3" width="10" height="10" filled="false" />
</draw_ops>

<!-- Minimize Button -->
<draw_ops name="btn_min_normal">
  <line color="C_btn_fg" x1="3" y1="9" x2="13" y2="9" width="1.5" />
</draw_ops>

<draw_ops name="btn_min_hover">
  <rectangle color="C_btn_bg_hover" x="0" y="0" width="width" height="height" filled="true" />
  <line color="#FFFFFF" x1="3" y1="9" x2="13" y2="9" width="1.8" />
</draw_ops>

<!-- ::: FRAME STYLES ::: -->
<frame_style name="focused" geometry="normal">
  <piece position="entire_background" style="draw_frame_focused" />
  <piece position="title" style="draw_frame_focused" />
  <button function="close" state="normal" draw_ops="btn_close_normal" />
  <button function="close" state="prelight" draw_ops="btn_close_hover" />
  <button function="maximize" state="normal" draw_ops="btn_max_normal" />
  <button function="maximize" state="prelight" draw_ops="btn_max_hover" />
  <button function="minimize" state="normal" draw_ops="btn_min_normal" />
  <button function="minimize" state="prelight" draw_ops="btn_min_hover" />
</frame_style>

<frame_style name="unfocused" geometry="normal">
  <piece position="entire_background" style="draw_frame_unfocused" />
  <button function="close" state="normal" draw_ops="btn_close_normal" />
  <button function="maximize" state="normal" draw_ops="btn_max_normal" />
  <button function="minimize" state="normal" draw_ops="btn_min_normal" />
</frame_style>

<frame_style_set name="normal">
  <frame focus="yes" state="normal" resize="both" style="focused" />
  <frame focus="no" state="normal" resize="both" style="unfocused" />
  <frame focus="yes" state="maximized" style="focused" />
  <frame focus="no" state="maximized" style="unfocused" />
</frame_style_set>

<window type="normal" style_set="normal" />
<window type="dialog" style_set="normal" />
<window type="modal_dialog" style_set="normal" />

</metacity_theme>
"""

with open(os.path.join(META_DIR, "metacity-theme-3.xml"), "w") as f:
    f.write(metacity_xml)

# 2. GTK 3.0 & GTK 4.0 CSS (Windows 11 Frosted Acrylic Headerbars)
gtk_css = """/* STARK INDUSTRIES // WINDOWS 11 GTK THEME */
@define-color theme_bg_color #080E18;
@define-color theme_fg_color #F0F6FC;
@define-color theme_base_color #0D1829;
@define-color theme_text_color #F0F6FC;
@define-color theme_selected_bg_color #00E5FF;
@define-color theme_selected_fg_color #070B14;
@define-color borders rgba(0, 229, 255, 0.35);

window, .background {
  background-color: @theme_bg_color;
  color: @theme_fg_color;
}

headerbar, .titlebar {
  background-color: rgba(8, 14, 24, 0.92);
  border-bottom: 1px solid rgba(0, 229, 255, 0.35);
  box-shadow: 0 4px 12px rgba(0, 0, 0, 0.4);
  padding: 4px 8px;
}

headerbar:backdrop, .titlebar:backdrop {
  background-color: #0A101C;
  color: #64748B;
}

headerbar button.titlebutton {
  min-width: 32px;
  min-height: 28px;
  padding: 4px;
  border-radius: 6px;
  background-color: transparent;
  color: #F0F6FC;
  transition: all 150ms ease;
}

headerbar button.titlebutton:hover {
  background-color: rgba(0, 229, 255, 0.18);
  color: #00E5FF;
}

headerbar button.titlebutton.close:hover {
  background-color: #E81123;
  color: #FFFFFF;
}

/* Windows 11 Entry Fields */
entry {
  background-color: rgba(255, 255, 255, 0.05);
  border: 1px solid rgba(0, 229, 255, 0.3);
  border-radius: 8px;
  color: #F0F6FC;
  padding: 6px 10px;
}

entry:focus {
  border-color: #00E5FF;
  box-shadow: 0 0 8px rgba(0, 229, 255, 0.4);
}

/* Switches & Toggles */
switch {
  background-color: rgba(255, 255, 255, 0.15);
  border-radius: 12px;
  border: 1px solid transparent;
}

switch:checked {
  background-color: #00E5FF;
}

switch slider {
  background-color: #FFFFFF;
  border-radius: 50%;
  min-width: 18px;
  min-height: 18px;
}
"""

with open(os.path.join(GTK3_DIR, "gtk.css"), "w") as f:
    f.write(gtk_css)
with open(os.path.join(GTK3_DIR, "gtk-dark.css"), "w") as f:
    f.write(gtk_css)
with open(os.path.join(GTK4_DIR, "gtk.css"), "w") as f:
    f.write(gtk_css)

# 3. Master index.theme linking Cinnamon, Metacity, GTK, and Icons
master_index_theme = """[Desktop Entry]
Type=X-GNOME-Metatheme
Name=Jarvis-Windows11-Shell
Comment=Stark Industries J.A.R.V.I.S. Windows 11 Desktop Shell Suite
Encoding=UTF-8

[X-GNOME-Metatheme]
GtkTheme=Jarvis-Windows11-Shell
MetacityTheme=Jarvis-Windows11-Shell
IconTheme=Jarvis-White
CinnamonTheme=Jarvis-Windows11-Shell
"""

with open(os.path.join(THEME_ROOT, "index.theme"), "w") as f:
    f.write(master_index_theme)

print("[WINDOW DECORATION ENGINE]: Successfully generated Metacity-1 and GTK-3.0/4.0 decoration suite.")
