### Section: Admin Panel

#### Interactive UI Elements Identified:

1. **Buttons (ttk.Button)**
   - "☰" (Menu button)
   - "Server Monitor"
   - "Run" (with "Green.TButton" style)
   - "Disable" (Auto-Backup control)
   - "Enable" (with "Orange.TButton" style, Auto-Update control)
   - "📄", "🔄", "📊", "❓" (Utility buttons)
   - Close buttons for tabs: "×"
   - Add Tab button: "+"
   - "Create Support Zip", "Sync", "Import", "Save" (Profile Section)
   - "ℹ" (Information button)
   - "Install"
   - "📁" (Folder icon button)
   - "Set Location..."
   - "Start"
   - "Players"

2. **Entry Fields (ttk.Entry)**
   - IP Address entry field ("My Public IP")
   - Profile name entry field (default "Unnamed Profile")

3. **Labels (ttk.Label)**
   - Static informational text (e.g., "Version:", "My Public IP:", "Auto-Backup:", "Status: Uninstalled", etc.)
   - Status indicators with color (e.g., "Ready" in green, "Disabled" in orange)

4. **Listbox (tk.Listbox)**
   - Sidebar section list (populated with the different sections)

5. **Scrollbar (ttk.Scrollbar)**
   - Vertical scrollbar linked to the Listbox

6. **Notebook Tabs (ttk.Notebook)**
   - Default Tab
   - Dynamically added tabs (e.g., "Tab 1", "Tab 2", etc.)

7. **Paned Window (ttk.PanedWindow)**
   - Adjustable sections dividing the sidebar and content area

#### Notes on Default Purposes:
- Buttons like "☰", "📄", "🔄", "📊", "❓" serve distinct utility functions despite being similar button elements.
- Status labels differentiate by color to represent various states (green for "Ready", orange for "Disabled").
- The Notebook supports dynamic tab creation with unique close buttons for each tab.

### Section: Admin Panel

#### Interactive UI Elements Identified:

1. **Buttons (ttk.Button)**
   - "☰" (Menu button)
   - "Server Monitor"
   - "Run" (with "Green.TButton" style)
   - "Disable" (Auto-Backup control)
   - "Enable" (with "Orange.TButton" style, Auto-Update control)
   - "📄", "🔄", "📊", "❓" (Utility buttons)
   - Close buttons for tabs: "×"
   - Add Tab button: "+"
   - "Create Support Zip", "Sync", "Import", "Save" (Profile Section)
   - "ℹ" (Information button)
   - "Install"
   - "📁" (Folder icon button)
   - "Set Location..."
   - "Start"
   - "Players"

2. **Entry Fields (ttk.Entry)**
   - IP Address entry field ("My Public IP")
   - Profile name entry field (default "Unnamed Profile")

3. **Labels (ttk.Label)**
   - Static informational text (e.g., "Version:", "My Public IP:", "Auto-Backup:", "Status: Uninstalled", etc.)
   - Status indicators with color (e.g., "Ready" in green, "Disabled" in orange)

4. **Listbox (tk.Listbox)**
   - Sidebar section list (populated with the different sections)

5. **Scrollbar (ttk.Scrollbar)**
   - Vertical scrollbar linked to the Listbox

6. **Notebook Tabs (ttk.Notebook)**
   - Default Tab
   - Dynamically added tabs (e.g., "Tab 1", "Tab 2", etc.)

7. **Paned Window (ttk.PanedWindow)**
   - Adjustable sections dividing the sidebar and content area

#### Notes on Default Purposes:
- Buttons like "☰", "📄", "🔄", "📊", "❓" serve distinct utility functions despite being similar button elements.
- Status labels differentiate by color to represent various states (green for "Ready", orange for "Disabled").
- The Notebook supports dynamic tab creation with unique close buttons for each tab.

### Section: Admin Content

#### Interactive UI Elements Identified:

1. **Buttons (ttk.Button)**
   - "↻" (Networking refresh button)
   - "📁" (Map Mod Path and Total Conversion ID browse buttons)
   - "Browse" (Mod IDs browse button)
   - "Download" (Mod IDs download button)
   - "Backup Now" (Saves section)
   - "Restore..." (Saves section)
   - "..." (Command Line section button)
   - "Show Command..." (Command Line section button)

2. **Entry Fields (ttk.Entry)**
   - Server Name
   - Server Password (masked)
   - Admin Password (masked)
   - Spectator Password (masked)
   - Server Port
   - Peer Port
   - Query Port
   - RCON Port
   - RCON Server Log Buffer
   - Mod IDs
   - Auto Save Period
   - Max Players
   - Idle Timeout
   - Auto Force Respawn Interval
   - Alternate Save Directory
   - Cross-ARK Data Transfer ClusterId
   - Web Key (masked)
   - Web URL (masked)
   - Branch Name
   - Branch Password (masked)
   - Affinity - CPU
   - Launcher Args
   - Server Args

3. **Labels (ttk.Label)**
   - Informational text (e.g., "Server Name:", "Server Password:", "Local IP:", "Auto Save Period:", "Max Players:", "Status:", etc.)
   - Dynamic counters (e.g., "Length: 0", "Lines: 0")

4. **Combobox (ttk.Combobox)**
   - Local IP selection
   - Map Name or Mod Path selection
   - Total Conversion ID selection
   - Branch Name selection
   - Priority selection

5. **Checkbuttons (ttk.Checkbutton)**
   - Enable RCON
   - Override Launcher
   - Cluster Directory Override
   - Multiple server option toggles (e.g., "Use Ban List URL", "Disable VAC", "Enable BattlEye", etc.)

6. **Text Box (tk.Text)**
   - Message of the Day (MOTD) text box

7. **Scrollbar (ttk.Scrollbar)**
   - Scrollbar linked to the MOTD text box

8. **Scale (ttk.Scale)**
   - Auto Save Period
   - Max Players
   - Auto Force Respawn Interval

#### Notes on Default Purposes:
- Checkbuttons are used extensively for toggling server options with default labels describing each specific functionality.
- The masked Entry fields are specifically for password or sensitive data inputs.
- The combination of Scale and Entry fields allows precise numeric adjustments and direct input.

### Section: Automatic Management

#### Interactive UI Elements Identified:

1. **Buttons (ttk.Button)**
   - None explicitly defined beyond scrollbar control.

2. **Entry Fields (ttk.Entry)**
   - Shutdown Time Entry (default "00:00")

3. **Labels (ttk.Label)**
   - Day Labels: "Sun", "Mon", "Tue", "Wed", "Thu", "Fri", "Sat"

4. **Checkbuttons (ttk.Checkbutton)**
   - Auto-Start server on boot
   - Include server in the Auto-Backup cycle
   - Include server in the Auto-Update cycle
   - Restart server if shutdown
   - Shutdown server at (per schedule)
   - Perform update (per schedule)
   - Then restart (per schedule)
   - Day selection checkboxes for each day of the week

5. **Scrollbar (ttk.Scrollbar)**
   - Vertical scrollbar linked to the scrollable frame

#### Notes on Default Purposes:
- The shutdown schedule utilizes paired Checkbuttons and Entry fields to manage timing and operational automation.
- Day labels with corresponding checkboxes allow flexible weekly scheduling.

### Section: Rules Content

#### Interactive UI Elements Identified:

1. **Buttons (ttk.Button)**
   - None explicitly defined beyond scrollbar control.

2. **Entry Fields (ttk.Entry)**
   - Time Input Fields (validated as "HH:MM", default "00:00")
   - Slider Value Entry Fields (paired with sliders)

3. **Labels (ttk.Label)**
   - Static text labels for descriptions and settings
   - Day Labels: "Sun", "Mon", "Tue", "Wed", "Thu", "Fri", "Sat"
   - Warning Label (distinct red text for item stat clamps)

4. **Checkbuttons (ttk.Checkbutton)**
   - General Rules toggles (e.g., "Enable Hardcore Mode", "Enable PvP")
   - Tribute Options (e.g., "No Survivor Uploads", "No Item Uploads")
   - Cluster Tribute Options (e.g., "No Transfer from Filtering", "Prevent Offline PvP")
   - PvE Schedule toggles (e.g., "PvE Schedule", "Use Server Time")
   - Tribe Settings and Tribe Warfare Options (e.g., "Allow Tribe Alliances", "Allow Tribe Warfare")
   - Disease and Network Settings (e.g., "Enable Diseases", "Non Permanent Diseases")
   - Cryopod Settings (e.g., "Enable Cryopod Nerf")
   - Genesis Part 1 & 2 (e.g., "Disable Missions", "Allow TEK Suit Powers")
   - Hexagon Settings (e.g., "Disable Hexagon Store", "Allow Only Engram Points Trade")
   - Item Stat Clamps (paired with sliders and entries)

5. **Sliders (ttk.Scale)**
   - Settings with adjustable ranges (e.g., "Supply Crate Loot Quality Multiplier", "Max Dino Level")
   - Sliders paired with entry fields for precise control

6. **Scrollbar (ttk.Scrollbar)**
   - Vertical scrollbar linked to the scrollable frame

#### Notes on Default Purposes:
- Sliders are often paired with entry fields for both coarse and fine adjustments.
- Checkbuttons are used extensively to enable/disable features across different game mechanics.
- Time input fields have built-in validation to ensure proper "HH:MM" format.
- Warning labels in red text provide critical notices to the user, especially in sensitive sections like "Item Stat Clamps."

### Section: Chat and Notifications

#### Interactive UI Elements Identified:

1. **Buttons (ttk.Button)**
   - None explicitly defined beyond scrollbar control.

2. **Labels (ttk.Label)**
   - Section Label: "Chat and Notifications"

3. **Checkbuttons (ttk.Checkbutton)**
   - Enable Global Voice Chat
   - Enable Proximity Text Chat
   - Enable 'Player Left' Notifications
   - Enable 'Player Joined' Notifications

4. **Scrollbar (ttk.Scrollbar)**
   - Vertical scrollbar linked to the scrollable frame

#### Notes on Default Purposes:
- Checkbuttons are used to toggle various chat and notification settings, organized into left and right columns for better clarity.
- The scrollbar facilitates navigation within the scrollable content area.

### Section: HUD and Visuals

#### Interactive UI Elements Identified:

1. **Buttons (ttk.Button)**
   - None explicitly defined beyond scrollbar control.

2. **Labels (ttk.Label)**
   - Section Label: "HUD and Visuals"

3. **Checkbuttons (ttk.Checkbutton)**
   - Allow Crosshair
   - Allow HUD
   - Allow Map Player Location
   - Allow Third-Person View
   - Show Floating Damage Text
   - Allow Hit Markers
   - Allow Player Gamma Settings in PvP
   - Allow Player Gamma Settings in PvE

4. **Scrollbar (ttk.Scrollbar)**
   - Vertical scrollbar linked to the scrollable frame

#### Notes on Default Purposes:
- Checkbuttons are used to toggle various HUD and visual settings, organized into left, middle, and right columns for better clarity.
- The scrollbar facilitates navigation within the scrollable content area.

### Section: Player Settings

#### Interactive UI Elements Identified:

1. **Buttons (ttk.Button)**
   - None explicitly defined beyond scrollbar control.

2. **Labels (ttk.Label)**
   - Section Labels: "Player Settings", "Base Stat Multipliers", "Per-Level Stat Multipliers"
   - Stat Labels for each slider (e.g., "XP Multiplier", "Health", "Stamina")

3. **Checkbuttons (ttk.Checkbutton)**
   - Enable Flyer-Carry
   - Base Stat Multipliers (main toggle)
   - Per-Level Stat Multipliers (main toggle)

4. **Sliders (ttk.Scale)**
   - Player multipliers (e.g., "XP Multiplier", "Damage", "Resistance")
   - Base stat multipliers (e.g., "Health", "Stamina", "Torpidity", "Oxygen")
   - Per-level stat multipliers (e.g., "Health", "Stamina", "Oxygen")

5. **Entry Fields (ttk.Entry)**
   - Paired with each slider for precise value input

6. **Scrollbar (ttk.Scrollbar)**
   - Vertical scrollbar linked to the scrollable frame

#### Notes on Default Purposes:
- Sliders are used to adjust player-related multipliers with associated entry fields for direct value input.
- Checkbuttons are used to toggle specific features or enable entire sections of multipliers.
- Labels provide context for sliders and checkboxes, ensuring clarity in functionality.
- The scrollbar facilitates navigation within the scrollable content area.

### Section: Player Settings

#### Interactive UI Elements Identified:

1. **Buttons (ttk.Button)**
   - None explicitly defined beyond scrollbar control.

2. **Labels (ttk.Label)**
   - Section Labels: "Player Settings", "Base Stat Multipliers", "Per-Level Stat Multipliers"
   - Stat Labels for each slider (e.g., "XP Multiplier", "Health", "Stamina")

3. **Checkbuttons (ttk.Checkbutton)**
   - Enable Flyer-Carry
   - Base Stat Multipliers (main toggle)
   - Per-Level Stat Multipliers (main toggle)

4. **Sliders (ttk.Scale)**
   - Player multipliers (e.g., "XP Multiplier", "Damage", "Resistance")
   - Base stat multipliers (e.g., "Health", "Stamina", "Torpidity", "Oxygen")
   - Per-level stat multipliers (e.g., "Health", "Stamina", "Oxygen")

5. **Entry Fields (ttk.Entry)**
   - Paired with each slider for precise value input

6. **Scrollbar (ttk.Scrollbar)**
   - Vertical scrollbar linked to the scrollable frame

#### Notes on Default Purposes:
- Sliders are used to adjust player-related multipliers with associated entry fields for direct value input.
- Checkbuttons are used to toggle specific features or enable entire sections of multipliers.
- Labels provide context for sliders and checkboxes, ensuring clarity in functionality.
- The scrollbar facilitates navigation within the scrollable content area.

---

### Section: Dino Settings

#### Interactive UI Elements Identified:

1. **Buttons (ttk.Button)**
   - None explicitly defined beyond scrollbar control.

2. **Labels (ttk.Label)**
   - Section Labels: "Dino Counts", "Base Dino Stats", "Tame Settings", "Additional Stats", "Raid Settings", "Flyer Settings", "Riding Settings", "Dino Customization", "Dino Configuration", "Per-Level Stat Multipliers (Wild)", "Per-Level Stat Multipliers (Tamed)", "Per-Level Stat Multipliers (Tamed) - Add", "Per-Level Stat Multipliers (Tamed) - Affinity", "Dino Breeding Multipliers", "Dino Imprinting"
   - Stat Labels for each slider (e.g., "Damage", "Resistance", "Food Drain")

3. **Checkbuttons (ttk.Checkbutton)**
   - Various settings toggles under Flyer Settings, Riding Settings, Customization, Raid Settings, Imprinting, and more (e.g., "Allow Flyers in Caves", "Allow Flying Stamina Recovery", "Disable Dino Riding")

4. **Sliders (ttk.Scale)**
   - Dino-related multipliers (e.g., "Max Tamed Dinos", "Damage", "Resistance", "Passive Tame Interval")
   - Breeding and imprinting multipliers (e.g., "Mating Interval", "Egg Hatch Speed", "Cuddle Interval")

5. **Entry Fields (ttk.Entry)**
   - Paired with each slider for precise value input

6. **Combobox (ttk.Combobox)**
   - Used for filtering options in the Dino Customization section

7. **Treeview (ttk.Treeview)**
   - Displays the Dino Configuration table with columns: Name, Mod, Spawnable, Tameable, Replace With

8. **Scrollbar (ttk.Scrollbar)**
   - Vertical scrollbar linked to both the main scrollable frame and the Dino Configuration Treeview

#### Notes on Default Purposes:
- Sliders are used extensively to adjust dino-related multipliers and configurations with associated entry fields for specific value input.
- Checkbuttons enable/disable specific features or options across dino mechanics.
- Labels provide structure and clarity for each section.
- The Treeview component allows for a structured display of dino configurations with scroll functionality.
- The scrollbar aids in navigating through the expansive list of settings.

### Section: Player Settings

#### Interactive UI Elements Identified:

1. **Buttons (ttk.Button)**
   - None explicitly defined beyond scrollbar control.

2. **Labels (ttk.Label)**
   - Section Labels: "Player Settings", "Base Stat Multipliers", "Per-Level Stat Multipliers"
   - Stat Labels for each slider (e.g., "XP Multiplier", "Health", "Stamina")

3. **Checkbuttons (ttk.Checkbutton)**
   - Enable Flyer-Carry
   - Base Stat Multipliers (main toggle)
   - Per-Level Stat Multipliers (main toggle)

4. **Sliders (ttk.Scale)**
   - Player multipliers (e.g., "XP Multiplier", "Damage", "Resistance")
   - Base stat multipliers (e.g., "Health", "Stamina", "Torpidity", "Oxygen")
   - Per-level stat multipliers (e.g., "Health", "Stamina", "Oxygen")

5. **Entry Fields (ttk.Entry)**
   - Paired with each slider for precise value input

6. **Scrollbar (ttk.Scrollbar)**
   - Vertical scrollbar linked to the scrollable frame

#### Notes on Default Purposes:
- Sliders are used to adjust player-related multipliers with associated entry fields for direct value input.
- Checkbuttons are used to toggle specific features or enable entire sections of multipliers.
- Labels provide context for sliders and checkboxes, ensuring clarity in functionality.
- The scrollbar facilitates navigation within the scrollable content area.

---

### Section: Dino Settings

#### Interactive UI Elements Identified:

1. **Buttons (ttk.Button)**
   - None explicitly defined beyond scrollbar control.

2. **Labels (ttk.Label)**
   - Section Labels: "Dino Counts", "Base Dino Stats", "Tame Settings", "Additional Stats", "Raid Settings", "Flyer Settings", "Riding Settings", "Dino Customization", "Dino Configuration", "Per-Level Stat Multipliers (Wild)", "Per-Level Stat Multipliers (Tamed)", "Per-Level Stat Multipliers (Tamed) - Add", "Per-Level Stat Multipliers (Tamed) - Affinity", "Dino Breeding Multipliers", "Dino Imprinting"
   - Stat Labels for each slider (e.g., "Damage", "Resistance", "Food Drain")

3. **Checkbuttons (ttk.Checkbutton)**
   - Various settings toggles under Flyer Settings, Riding Settings, Customization, Raid Settings, Imprinting, and more (e.g., "Allow Flyers in Caves", "Allow Flying Stamina Recovery", "Disable Dino Riding")

4. **Sliders (ttk.Scale)**
   - Dino-related multipliers (e.g., "Max Tamed Dinos", "Damage", "Resistance", "Passive Tame Interval")
   - Breeding and imprinting multipliers (e.g., "Mating Interval", "Egg Hatch Speed", "Cuddle Interval")

5. **Entry Fields (ttk.Entry)**
   - Paired with each slider for precise value input

6. **Combobox (ttk.Combobox)**
   - Used for filtering options in the Dino Customization section

7. **Treeview (ttk.Treeview)**
   - Displays the Dino Configuration table with columns: Name, Mod, Spawnable, Tameable, Replace With

8. **Scrollbar (ttk.Scrollbar)**
   - Vertical scrollbar linked to both the main scrollable frame and the Dino Configuration Treeview

#### Notes on Default Purposes:
- Sliders are used extensively to adjust dino-related multipliers and configurations with associated entry fields for specific value input.
- Checkbuttons enable/disable specific features or options across dino mechanics.
- Labels provide structure and clarity for each section.
- The Treeview component allows for a structured display of dino configurations with scroll functionality.
- The scrollbar aids in navigating through the expansive list of settings.

---

### Section: Environment Settings

#### Interactive UI Elements Identified:

1. **Buttons (ttk.Button)**
   - None explicitly defined beyond scrollbar control.

2. **Labels (ttk.Label)**
   - Section Labels: "Resource Settings", "Harvest Options", "Custom Harvest Configuration", "Time and Weather Settings", "Decomposition Settings", "Growth and Intervals", "Earned XP Multipliers"
   - Stat Labels for each slider (e.g., "Dino Spawns", "Taming Speed", "Harvest Amount")

3. **Checkbuttons (ttk.Checkbutton)**
   - Toggles for specific environment-related settings (e.g., "Clamp Resource Harvest Damage", "Disable Weather - Fog", "Clamp Item Spoiling Times")

4. **Sliders (ttk.Scale)**
   - Environment multipliers (e.g., "Dino Spawns", "Harvest Amount", "Day Cycle Speed")
   - Decomposition and growth rates (e.g., "Global Spoiling Time", "Crop Growth Speed")

5. **Entry Fields (ttk.Entry)**
   - Paired with each slider for precise value input

6. **Combobox (ttk.Combobox)**
   - Used for filtering options in the Custom Harvest Configuration section

7. **Treeview (ttk.Treeview)**
   - Displays the Custom Harvest Configuration table with columns: Name, Source, Amount Type, Amount

8. **Scrollbar (ttk.Scrollbar)**
   - Vertical scrollbar linked to both the main scrollable frame and the Custom Harvest Configuration Treeview

#### Notes on Default Purposes:
- Sliders adjust environment-related multipliers and timings with paired entry fields for precision.
- Checkbuttons toggle specific environmental features like weather effects or resource settings.
- Labels provide clear context for each setting and slider.
- The Treeview structure is used to organize custom harvest configurations with scroll support.
- The scrollbar ensures smooth navigation through the settings interface.

Section: Structures Settings

Interactive UI Elements Identified:

Buttons (ttk.Button)

None explicitly defined beyond scrollbar control.

Labels (ttk.Label)

Section Labels: "Basic Structure Settings", "PvP Structure Settings", "Structure Limits", "Platform Options", "Decay Settings", "Auto Destroy Settings", "Defense Settings", "Structure Pickup", "Genesis: Part 1"

Stat Labels for each slider (e.g., "Structure Resistance", "Structure Damage", "Auto Destroy Old Structures Multiplier")

Checkbuttons (ttk.Checkbutton)

Toggles for structure-related settings (e.g., "Disable Structure Placement Collision", "Enable PvP Structure Decay", "Auto Destroy Structures")

Sliders (ttk.Scale)

Structure multipliers and settings (e.g., "Structure Damage Repair Cooldown", "PvP Zone Structure Damage", "Per-Platform Structures Multiplier")

Entry Fields (ttk.Entry)

Paired with each slider for precise value input

Scrollbar (ttk.Scrollbar)

Vertical scrollbar linked to the scrollable frame

Notes on Default Purposes:

Sliders are used to adjust structure-related multipliers and time-based settings, with paired entry fields for precise value adjustments.

Checkbuttons toggle structure-related features, such as decay, auto-destroy, and PvP settings.

Labels ensure clarity by providing context for each setting and slider.

The scrollbar facilitates smooth navigation through the settings interface.

### Section: EngramsPanel

**Interactive Elements Identified:**

1. **Checkbuttons:**
   - Auto Unlock All Engrams
   - Enable Engram Overrides
   - Only Allow Selected Engrams

2. **Buttons:**
   - ↻ (likely for refresh or reset functionality)
   - □ (could represent stop or clear)
   - ▤ (possibly represents menu or options)
   - ↑ (typically indicates upward action, like move up)
   - ↓ (typically indicates downward action, like move down)
   - 🔍 (commonly used for search functionality)

3. **Combobox:**
   - Filter selection with default value "All"

4. **Entry (Text Input):**
   - Filter entry for user to type text (likely used for searching or filtering)

5. **Treeview:**
   - Displays data in a tabular format with headings:
     - Name
     - Mod
     - Is Tekgram
     - Level
     - Cost
     - Hidden
     - Remove Prereqs
     - Auto Unlock
     - Unlock Level
   - Supports vertical and horizontal scrolling (via Scrollbars)

6. **Scrollbars:**
   - Vertical Scrollbar for the main canvas
   - Vertical and Horizontal Scrollbars for the Treeview

**Notes:**
- Each Checkbutton and Button has a unique label, suggesting distinct functionalities.
- The Treeview has sample data and alternating row colors for better readability.
- The Filter Combobox allows predefined selections, while the Entry field enables free-text input.
- Scrollbars are associated with both the main canvas and the Treeview for enhanced navigation.

### Section: ServerFileDetailsPanel

**Interactive Elements Identified:**

1. **Labels:**
   - Warning Label: "NOTE: Any changes will require a server restart to take effect." (bold text)

2. **Checkbuttons:**
   - Enable Exclusive Join

3. **Buttons:**
   - + (typically used for adding items)
   - × (typically used for removing items)
   - ↻ (likely for refresh functionality)

4. **Treeview:**
   - Displays player data with columns:
     - Player Id
     - Player Name
   - Supports vertical scrolling (via Scrollbar)

5. **Scrollbars:**
   - Vertical Scrollbar for each Treeview to support navigation through player lists

**Panels Identified:**
- **Administrators Panel:** Includes control buttons (+, ×, ↻) and a player list view
- **Whitelisted Panel:** Similar structure with control buttons and player list view
- **Exclusive Join Panel:** Includes Enable Exclusive Join checkbox, control buttons, and player list view

**Notes:**
- Each panel shares a common structure with control buttons and list views, providing consistency in user interaction.
- The Enable Exclusive Join checkbox is unique to the Exclusive Join Panel.
- The Treeview elements allow for dynamic data display with scroll support, enhancing usability for large datasets.

### Section: CustomSettingsPanel

**Interactive Elements Identified:**

1. **Buttons:**
   - **Custom Sections Panel:**
     - ↻ (likely for refresh functionality)
     - + (typically used for adding items)
     - □ (possibly represents stop, clear, or reset)
     - ↓ (typically indicates downward action, like move down)
     - × (typically used for removing items)
   - **Custom Items Panel:**
     - + (for adding items)
     - □ (possibly for clearing or resetting)
     - × (for removing items)

2. **Treeview:**
   - **Custom Sections Panel:**
     - Displays section names with a single column:
       - Section Name
     - Supports vertical scrolling (via Scrollbar)
   - **Custom Items Panel:**
     - Displays key-value pairs with columns:
       - Key
       - Value
     - Supports vertical scrolling (via Scrollbar)

3. **Scrollbars:**
   - Vertical Scrollbars for each Treeview to support navigation through lists

**Panels Identified:**
- **Custom Sections Panel:** Contains toolbar with control buttons and a Treeview for section names
- **Custom Items Panel:** Includes a toolbar with control buttons and a Treeview for key-value items

**Notes:**
- Each panel provides functionality for managing custom settings with consistent button layouts for ease of use.
- Treeview elements are used for structured data display with scroll support, enhancing navigation for large datasets.
- The duplication of buttons like +, □, and × across both panels suggests a similar interaction model for managing different data types.

### Section: LevelProgressionsPanel

**Interactive Elements Identified:**

1. **Labels:**
   - "Player Max XP:" (associated with controls)
   - "Dino Max XP:" (associated with controls)
   - Warning Note: Provides important information regarding player levels and ascension (wrapped text)

2. **Checkbuttons:**
   - Player Max XP (used to enable/disable XP settings)
   - Dino Max XP (used to enable/disable XP settings)
   - Enable Custom Level Progressions
   - Enable Dino Level Progressions

3. **Buttons:**
   - **Top Controls:**
     - ↻ (refresh/reset functionality for Player and Dino XP)
   - **Custom Player Levels Panel:**
     - × (remove/delete functionality)
     - ↻ (refresh/reset functionality)
     - 📝 (edit functionality)
     - ↓ (move down)
     - ↑ (move up)
   - **Custom Dino Levels Panel:**
     - × (remove/delete functionality)
     - ↻ (refresh/reset functionality)
     - 📝 (edit functionality)
     - ↓ (move down)
     - ↑ (move up)

4. **Scales (Sliders):**
   - Player Max XP Scale (range 0 to 100, horizontal orientation)
   - Dino Max XP Scale (range 0 to 100, horizontal orientation)

5. **Entry (Text Inputs):**
   - Player XP Entry (default value "5")
   - Dino XP Entry (default value "10")

6. **Treeview:**
   - **Custom Player Levels:**
     - Columns: Level, XP Required, Engram Points, Engram Total
     - Displays sample data for player level progression
   - **Custom Dino Levels:**
     - Columns: Level, XP Required
     - Displays sample data for dino level progression

7. **Scrollbars:**
   - Vertical Scrollbars for both Player and Dino Treeviews for navigation through level data

**Panels Identified:**
- **Custom Player Levels Panel:** Includes control buttons, level progression treeview with engram data
- **Custom Dino Levels Panel:** Includes control buttons, level progression treeview without engram data

**Notes:**
- Consistent button layouts across Player and Dino panels provide a familiar interaction model
- Treeview elements allow for structured data display with vertical scroll support for extensive datasets
- Scales, Checkbuttons, and Entry widgets enhance the ability to customize XP-related settings
- The warning note ensures users are aware of the implications when modifying player levels, improving usability and preventing configuration errors

### Section: CraftingOverridesPanel

**Interactive Elements Identified:**

1. **Labels:**
   - **Warning Notes:**
     - Green Note: Provides information about managing overrides manually.
     - Regular Note: Informs about the requirement to relearn engrams after resource changes.

2. **Buttons:**
   - **Crafted Items Panel:**
     - + (for adding crafted items)
     - □ (likely for clearing or resetting)
     - × (for removing items)
     - ⎘ (copy or duplicate functionality)
   - **Resource Items Panel:**
     - + (for adding resource items)
     - × (for removing resource items)

3. **Treeview:**
   - **Crafted Items Panel:**
     - Columns:
       - Crafted Item
     - Displays crafted items list with vertical scrolling support
   - **Resource Items Panel:**
     - Columns:
       - Resource Item
       - Quantity
       - Require Exact Resource Type
     - Displays resource items with details and vertical scrolling support

4. **Scrollbars:**
   - Vertical Scrollbars for both Crafted Items and Resource Items Treeviews for better navigation through extensive data

**Panels Identified:**
- **Crafted Items Panel:** Includes control buttons, crafted items list displayed in a Treeview
- **Resource Items Panel:** Contains control buttons and a Treeview for managing resource items with details on quantity and exact resource requirements

**Notes:**
- The crafted items panel allows more detailed item management, including copy functionality (⎘), which is not present in the resource items panel
- Treeviews in both panels are designed for structured data presentation, complemented by scrollbars for ease of navigation
- Warning notes enhance usability by providing critical information related to managing crafting overrides and engram dependencies

### Section: StackSizeOverridesPanel

**Interactive Elements Identified:**

1. **Labels:**
   - **Warning Note:** Provides information about managing overrides manually.
   - **Global Multiplier:**
     - "Item Stack Size Multiplier"
     - "x" (label indicating multiplier factor)

2. **Scale (Slider):**
   - Item Stack Size Multiplier (range from 0 to 100, horizontal orientation, default value set to 1)

3. **Entry (Text Input):**
   - Text Entry linked to the stack size multiplier with a default value of "1"

4. **Buttons:**
   - **Stacked Items Panel:**
     - + (for adding new items)
     - □ (possibly for clearing or resetting items)
     - × (for removing items)
     - ⎘ (copy or duplicate functionality)

5. **Treeview:**
   - **Stacked Items Panel:**
     - Columns:
       - Item
       - Max Item Quantity
       - Ignore Multiplier
     - Displays stacked items list with vertical scrolling support

6. **Scrollbars:**
   - Vertical Scrollbar for the Treeview to facilitate navigation through the item list

**Panels Identified:**
- **Stacked Items Panel:** Contains control buttons and a Treeview for managing stacked items with details on quantity and multiplier options

**Notes:**
- The combination of the slider and entry box allows for both quick and precise adjustments to the stack size multiplier
- Treeview provides a structured format to manage multiple items, complemented by control buttons for item management
- The warning note helps users understand configuration dependencies, ensuring proper management of stack size overrides

### Section: MapSpawnerOverridesPanel

**Interactive Elements Identified:**

1. **Labels:**
   - **Warning Note:** Provides information about managing overrides manually.

2. **Buttons:**
   - **Containers Panel:**
     - + (for adding new containers)
     - □ (possibly for clearing or resetting containers)
     - × (for removing containers)
     - ⎘ (copy or duplicate functionality)
   - **Entries Panel:**
     - + (for adding new entries)
     - × (for removing entries)

3. **Treeview:**
   - **Containers Panel:**
     - Columns:
       - Type
       - Spawner
     - Displays container types and associated spawners with vertical scrolling support
   - **Entries Panel:**
     - Columns:
       - Name
       - Dino
       - Weight
       - Max Percentage
     - Displays entries related to dino spawning configurations with vertical scrolling support

4. **Scrollbars:**
   - Vertical Scrollbars for both Containers and Entries Treeviews to facilitate navigation through lists

**Panels Identified:**
- **Containers Panel:** Includes control buttons and a Treeview for managing containers and spawners
- **Entries Panel:** Contains control buttons and a Treeview for managing dino spawn entries and related attributes

**Notes:**
- Treeviews provide a structured format for managing spawner-related data, complemented by control buttons for easy item manipulation
- The warning note enhances usability by guiding users on configuration management options, ensuring they are aware of potential overrides
- Consistent button layouts across both panels ensure familiarity and ease of use when managing different data types

### Section: SupplyCrateOverridesPanel

**Interactive Elements Identified:**

1. **Labels:**
   - **Warning Notes:**
     - Green Note: Provides information about managing overrides manually.
     - Red Note: Warning regarding proper grid population to ensure supply crates spawn correctly.

2. **Buttons:**
   - **Supply Crates Panel:**
     - + (for adding new supply crates)
     - □ (possibly for clearing or resetting supply crates)
     - × (for removing supply crates)
     - ⎘ (copy or duplicate functionality)
   - **Item Sets Panel:**
     - + (for adding new item sets)
     - × (for removing item sets)
   - **Item Set Entries Panel:**
     - + (for adding new item set entries)
     - × (for removing item set entries)
   - **Items Panel:**
     - + (for adding new items)
     - × (for removing items)

3. **Treeview:**
   - **Supply Crates Panel:**
     - Columns:
       - Supply Crate
       - Min ItemSets
       - Max ItemSets
       - Quality Multiplier
       - Prevent Duplicates
       - Append Item Sets
       - Prevent Increasing
   - **Item Sets Panel:**
     - Columns:
       - Description
       - Min Items
       - Max Items
       - Quality Multiplier
       - Weight
       - Prevent Duplicates
   - **Item Set Entries Panel:**
     - Columns:
       - Description
       - Min Quantity
       - Max Quantity
       - Min Quality
       - Max Quality
       - Weight
       - Force Blueprint
       - Blueprint Chance
   - **Items Panel:**
     - Columns:
       - Item
       - Weight

4. **Scrollbars:**
   - Vertical Scrollbars for all Treeview elements to facilitate navigation through extensive data lists

**Panels Identified:**
- **Supply Crates Panel:** Includes control buttons and a Treeview for managing supply crate configurations
- **Item Sets Panel:** Contains control buttons and a Treeview for managing item sets
- **Item Set Entries Panel:** Provides control buttons and a Treeview for managing specific entries within item sets
- **Items Panel:** Features control buttons and a Treeview for managing individual items

**Notes:**
- Treeviews provide structured data management with scrolling support, enhancing usability for large datasets
- Consistent button layouts across panels ensure ease of use and familiarity when managing different configurations
- The combination of warning notes, structured panels, and interactive elements promotes efficient configuration management and reduces user errors

### Section: PreventTransferOverridesPanel

**Interactive Elements Identified:**

1. **Labels:**
   - **Title Label:** "Prevent Transfer Overrides" (bold, larger font for header)
   - **Instruction Label:** Provides a note about manual management of overrides (blue text)
   - **Warning Label:** Warning about adding dinos to the list, preventing transfers (red text, bold font)

2. **Buttons:**
   - **Header Section:**
     - 🔄 (refresh functionality)
   - **Control Buttons Section:**
     - + (for adding new entries)
     - ✏️ (for editing existing entries)
     - ❌ (for removing entries)

3. **Treeview:**
   - **Data Table Section:**
     - Columns:
       - Dino
     - Displays entries related to dinos with an example row pre-inserted

4. **Scrollbars:**
   - Vertical Scrollbar for the Treeview to support navigation through the list

**Panels Identified:**
- **Header Section:** Displays the title and refresh button
- **Instruction Section:** Provides usage notes in blue text
- **Warning Section:** Alerts users about potential transfer issues with added dinos
- **Control Buttons Section:** Contains add, edit, and remove buttons for list management
- **Data Table Section:** Displays data in a Treeview with a scrollbar for ease of use

**Notes:**
- Consistent layout with clear sections enhances usability
- Use of colored text for instructions and warnings improves visibility and draws attention
- Control buttons allow easy management of dino transfer restrictions
- Treeview structure supports dynamic data display with scroll support for extensive lists