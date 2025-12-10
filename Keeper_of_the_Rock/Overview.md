# Keeper of the Rock

A 1970s narrative survival adventure about isolation, storms, and secrets at the world's loneliest lighthouse.

## About the Game

**Genre:** Narrative survival adventure, psychological mystery

**Setting:** Wolf Rock Lighthouse, Cornwall, England — Late 1970s (pre-automation, 1987)

**Engine:** Godot 4.2+

**Experience:** Solo, meditative, isolating, routine-driven, unnerving, contemplative

**Target Audience:** Players of *Firewatch*, *Dear Esther*, *The Long Dark*, and walking simulators with environmental storytelling

## Story

Late 1970s. You arrive at Wolf Rock Lighthouse — a granite tower rising from a submerged reef 8 miles off Land's End — for a routine one-week rotation. Weather shifts suddenly. Supply helicopters stop coming. Radio contact becomes sporadic, then impossible. Storms intensify beyond reason.

You discover hidden artwork scratched into walls, journals from keepers who never left, and remnants of tragedies spanning centuries. Historical events begin to echo in your dreams and bleed into your waking hours.

**Main Objective:** Survive the days, maintain the lighthouse, preserve your sanity, uncover the truth behind Wolf Rock's past, and ultimately escape the Rock.

## Unique Features

- Based on the **real Wolf Rock Lighthouse** and **documented historical events** spanning 600+ years
- A **psychological narrative** that blurs the line between reality and delusion
- A **seagull companion** that reacts to player behavior and serves as a tether to reality
- Strong **environmental storytelling** driven by storms, sound design, and the oppressive solitude of the sea
- **Historical authenticity** — real events (WWII U-boat wreck, 1394 shipwreck, 8-year construction) woven into gameplay

## Gameplay

**Daily Routine:**
- Check beacon (clean lens, light it)
- Log weather conditions
- Maintain generator, radio, lantern
- Cook and ration food
- Scan sea with binoculars — ships or… stranger things

**Random Events:**
- Storms damaging equipment or flooding rooms
- Mysterious radio calls
- Seagull visits (sometimes brings small objects)
- Dreams or hallucinations during long storms

**Exploration & Discovery:**
- Search for murals or sketches from past keepers
- Notes hidden in manuals or walls

## Roadmap

### Phase 1: Core Foundation (Complete)
- [x] Project setup with Godot 4.2+
- [x] First-person player controller with head bob
- [x] Lighthouse interior structure (5 floors + spiral staircase)
- [x] Time progression with day/night cycle
- [x] Sanity system with state thresholds
- [x] Resource tracking (food, fuel, radio battery)
- [x] Interaction framework (Interactable, ExaminableObject, UsableObject)
- [x] HUD connected to all manager systems
- [x] Save/load system with 3 slots + quick save/load (F5/F9)
- [x] EventBus for decoupled system communication

### Phase 2: Environment & Atmosphere (In Progress)
- [ ] **Weather System** — Dynamic storms, rain, wind, lightning
- [ ] **Ocean Rendering** — Wave simulation, multiple sea states, foam/spray
- [ ] **Volumetric Fog** — Atmosphere, visibility changes
- [ ] **Beacon Lighting** — Volumetric light rays, lens refraction, fog interaction
- [ ] **Lighthouse Props** — Furniture and equipment for each floor:
  - Level 1 (Storage): Emergency equipment, historical artifacts
  - Level 2 (Generator): Diesel generators, fuel tanks
  - Level 3 (Living Quarters): Bunks, kitchen, personal effects
  - Level 4 (Service Room): Radio equipment, weather station
  - Level 5 (Lantern Room): Beacon, glass panels, helipad access

### Phase 3: Audio & Immersion
- [ ] **Environmental Audio** — Waves, wind, storm sounds, seagulls
- [ ] **Interior Audio** — Generator hum, footsteps on different surfaces, doors
- [ ] **Radio System** — Tunable frequencies, static, period-appropriate music/news
- [ ] **Ambient Score** — Minimal, atmospheric music for key moments
- [ ] **Psychological Audio** — Whispers, metallic clangs (U-1209), impossible echoes

### Phase 4: Gameplay Systems
- [ ] **Seagull Companion AI** — Reactions to player behavior, brings objects, reality anchor
- [ ] **Daily Routine Tasks** — Beacon maintenance, weather logging, cooking
- [ ] **Equipment Interaction** — Generator operation, radio use, lantern maintenance
- [ ] **Journal System** — Weather logs, discoveries, objectives tracking
- [ ] **Binoculars** — Horizon scanning, ship spotting

### Phase 5: Sanity & Visual Effects
- [ ] **Sanity Shaders** — Screen distortion, color grading shifts
- [ ] **Hallucination System** — Visual/audio desync, unreliable UI
- [ ] **Dream Sequences** — Visions of historical events (U-1209, 1941 attack)
- [ ] **Object Anomalies** — Items appearing/disappearing, position shifts

### Phase 6: Narrative Content
- [ ] **Act I Implementation** — Days 1-5, tutorial, first anomalies
- [ ] **Discoverable Lore** — Past keeper journals, hidden artwork, artifacts
- [ ] **Radio Contacts** — Coastguard, other keeper, unidentified voices
- [ ] **Historical Echoes** — 1944 distress signals, 1906 fog tests, old weather reports

### Phase 7: Story Completion
- [ ] **Act II** — Escalation, major discoveries, stability challenges
- [ ] **Act III** — Breaking point, critical decisions
- [ ] **Act IV** — Multiple endings implementation:
  - Escape Ending (Reality Holds)
  - Keeper's Fate Ending (Succumb)
  - The Lighthouse Ending (Supernatural)
  - Historical Echo Ending (Ambiguous)

### Phase 8: Polish & Release
- [ ] **Accessibility Features** — Colorblind modes, subtitles, remappable controls
- [ ] **Settings Menu** — Graphics, audio, gameplay options
- [ ] **Achievements** — Historical reference achievements
- [ ] **Performance Optimization** — Target 60 FPS at 1080p
- [ ] **Playtesting & Bug Fixes**
- [ ] **itch.io Release**

## Current Status

Currently in **Phase 2** — Building out the environment and atmosphere systems that are central to the game's identity. Weather and ocean rendering are the next major milestones.

## Dev Blogs

### Idea Generation
[01-Idea generation](DevBlogs/01-Idea_generation.md)

## Follow the Game

_Coming soon to itch.io_

## Feedback

Feedback is always welcome! Reach out on Discord or email with ideas.
