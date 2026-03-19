---
title: DevUI Custom Theme Format
---

# DevUI Custom Theme Format

DevUI is the name of the ImGui implementation in Strata. DevUI supports custom themes provided in the `GAME` path under `resource/devui/themes`.
Themes are automatically indexed on game startup and can be changed at any time via the top menu bar, or via `devui_theme` in the console.

These are KeyValues 3 files with various properties defining different ImGui style parameters. Most of these match names in the
ImGuiStyle structure, `ImGuiCol_` enum and the `ImGuiStyleVar_` enum.

A functional example theme can be found in p2ce under `p2ce/resource/devui/themes/strata.kv3`.

```c
{
    // NOTE: The defaults presented here are not accurate. You will need to edit your own theme accordingly.

    // Font parameters
    Font = "panorama/fonts/LexendDeca-Regular.ttf" // Relative to the "GAME" search path.
    FontSize = 16

    // Float
    Alpha                               = 0.5
    DisabledAlpha                       = 0.5
    WindowRounding                      = 0.5
    WindowBorderSize                    = 0.5
    WindowBorderHoverPadding            = 0.5
    ChildRounding                       = 0.5
    ChildBorderSize                     = 0.5
    PopupRounding                       = 0.5
    PopupBorderSize                     = 0.5
    FrameRounding                       = 0.5
    FrameBorderSize                     = 0.5
    IndentSpacing                       = 0.5
    ColumnsMinSpacing                   = 0.5
    ScrollbarSize                       = 0.5
    ScrollbarRounding                   = 0.5
    GrabMinSize                         = 0.5
    GrabRounding                        = 0.5
    LogSliderDeadzone                   = 0.5
    ImageBorderSize                     = 0.5
    TabRounding                         = 0.5
    TabBorderSize                       = 0.5
    TabCloseButtonMinWidthSelected      = 0.5
    TabCloseButtonMinWidthUnselected    = 0.5
    TabBarBorderSize                    = 0.5
    TabBarOverlineSize                  = 0.5
    TableAngledHeadersAngle             = 0.5
    SeparatorTextBorderSize             = 0.5
    MouseCursorScale                    = 0.5
    CurveTessellationTol                = 0.5
    CircleTessellationMaxError          = 0.5
    HoverStationaryDelay                = 0.5
    HoverDelayShort                     = 0.5
    HoverDelayNormal                    = 0.5
    FontScaleDpi                        = 0.5
    FontScaleMain                       = 0.5
    FontSizeBase                        = 0.5

    // ImVec2 -- Specified as 2-component array
    WindowPadding           = [0.1, 0.1]
    WindowMinSize           = [0.1, 0.1]
    WindowTitleAlign        = [0.1, 0.1]
    FramePadding            = [0.1, 0.1]
    ItemSpacing             = [0.1, 0.1]
    ItemInnerSpacing        = [0.1, 0.1]
    CellPadding             = [0.1, 0.1]
    TouchExtraPadding       = [0.1, 0.1]
    ButtonTextAlign         = [0.1, 0.1]
    SelectableTextAlign     = [0.1, 0.1]
    SeparatorTextAlign      = [0.1, 0.1]
    SeparatorTextPadding    = [0.1, 0.1]
    DisplayWindowPadding    = [0.1, 0.1]
    DisplaySafeAreaPadding  = [0.1, 0.1]

    // ImGuiDir -- valid values: "up", "down", "left", "right", "none"
    WindowMenuButtonPosition = "up"
    ColorButtonPosition      = "up"
    
    // Bool
    AntiAliasedLines         = 0
    AntiAliasedLinesUseTex   = 0
    AntiAliasedFill          = 0
    
    // Colors -- May be 3/4 component hex or normalized float array
    //  Normalized float arrays have 3 or 4 components with values between 0 and 1.
    //  Hex colors must be prefixed by a '#' and are a string.
    Colors =
    {
        Text                   = [1.00, 1.00, 1.00, 1.00]
        TextDisabled           = [0.40, 0.40, 0.40, 1.00]
        ChildBg                = "#222222"
        WindowBg               = "#222222"
        PopupBg                = "#222222"
        Border                 = "#333333"
        BorderShadow           = [1.00, 1.00, 1.00, 0.06]
        FrameBg                = "#444444"
        FrameBgHovered         = "#666666"
        FrameBgActive          = "#444444"
        TitleBg                = "#a32b2b"
        TitleBgActive          = "#f0413c"
        TitleBgCollapsed       = "#a32b2baa"
        MenuBarBg              = "#222222"
        ScrollbarBg            = [0.24, 0.24, 0.24, 0.53]
        ScrollbarGrab          = [0.41, 0.41, 0.41, 1.00]
        ScrollbarGrabHovered   = [0.52, 0.52, 0.52, 1.00]
        ScrollbarGrabActive    = [0.76, 0.76, 0.76, 1.00]
        CheckMark              = [0.65, 0.65, 0.65, 1.00]
        SliderGrab             = "#f0413c"
        SliderGrabActive       = [0.64, 0.64, 0.64, 1.00]
        Button                 = [0.54, 0.54, 0.54, 0.35]
        ButtonHovered          = [0.52, 0.52, 0.52, 0.59]
        ButtonActive           = [0.76, 0.76, 0.76, 1.00]
        Header                 = [0.38, 0.38, 0.38, 1.00]
        HeaderHovered          = [0.47, 0.47, 0.47, 1.00]
        HeaderActive           = [0.76, 0.76, 0.76, 0.77]
        Separator              = [0.000, 0.000, 0.000, 0.137]
        SeparatorHovered       = [0.700, 0.671, 0.600, 0.290]
        SeparatorActive        = [0.702, 0.671, 0.600, 0.674]
        ResizeGrip             = "#f0413c"
        ResizeGripHovered      = "#a32b2b"
        ResizeGripActive       = "#a32b2b"
        PlotLines              = [0.61, 0.61, 0.61, 1.00]
        PlotLinesHovered       = [1.00, 0.43, 0.35, 1.00]
        PlotHistogram          = [0.90, 0.70, 0.00, 1.00]
        PlotHistogramHovered   = [1.00, 0.60, 0.00, 1.00]
        TextSelectedBg         = [0.73, 0.73, 0.73, 0.35]
        ModalWindowDimBg       = [0.80, 0.80, 0.80, 0.35]
        DragDropTarget         = [1.00, 1.00, 0.00, 0.90]
        NavHighlight           = [0.26, 0.59, 0.98, 1.00]
        NavWindowingHighlight  = [1.00, 1.00, 1.00, 0.70]
        NavWindowingDimBg      = [0.80, 0.80, 0.80, 0.20]
        DockingEmptyBg         = [0.38, 0.38, 0.38, 1.00]
        Tab                    = "#444444"
        TabHovered             = "#f0413c"
        TabActive              = "#f0413c"
        TabUnfocused           = "#ef8686"
        TabUnfocusedActive     = "#ef8686"
        DockingPreview         = [0.85, 0.85, 0.85, 0.28]
        TableRowBg             = "#222222"
        TableRowBgAlt          = "#333333"
    }
}
```