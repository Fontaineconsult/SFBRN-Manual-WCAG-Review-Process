# Test Log — 2026-07-adobe-express

One row per test run; details and evidence in `runs/<Run>/`.

| Run | Date | View | URL / location | Modality | Tool | Baseline | Task | Tester |
|-----|------|------|----------------|----------|------|----------|------|--------|
| R001 | 2026-07-27 19:23 | S1 | https://new.express.adobe.com/ | no-vision | jaws | B1 | P1 | — |
| R002 | 2026-08-04 15:44 | S1 | https://new.express.adobe.com/ | low-vision | zoom | B3 | — | — |
| R003 | 2026-08-04 15:44 | S1 | https://new.express.adobe.com/ | no-color | grayscale | — | — | — |
| R004 | 2026-08-04 15:44 | S1 | https://new.express.adobe.com/ | motor | keyboard | B2 | — | — |
| R005 | 2026-08-04 15:44 | S1 | https://new.express.adobe.com/ | no-hearing | inspection | — | — | — |
| R006 | 2026-08-04 15:44 | S1 | https://new.express.adobe.com/ | no-speech | inspection | — | — | — |
| R007 | 2026-08-04 16:21 | S1 | https://new.express.adobe.com/ | — | wave | — | — | — |
| R008 | 2026-08-04 16:32 | S1 | https://new.express.adobe.com/ | — | axe | — | — | — |
| R009 | 2026-08-04 16:38 | S1 | https://new.express.adobe.com/ | — | axe | — | — | — |
| R010 | 2026-08-06 12:15 | S1 | https://new.express.adobe.com/ | cognition | inspection | — | — | assistant (Claude, Chrome extension; DOM/animation instrumentation) |
| R011 | 2026-08-06 12:29 | S2 | https://new.express.adobe.com/explore/templates?assetCollection=urn%3Aaaid%3Asc%3AVA6C2%3A07c69ce7-24fd-488c-bac5-d18f464c5997 | — | axe | — | — | — |
| R012 | 2026-08-06 12:46 | S1 | https://new.express.adobe.com/ | no-vision | nvda | B4 | — | reviewer (D. Fontaine), NVDA 2026.1.1 + Chrome 150.0.7871.187 |
| R013 | 2026-08-06 14:18 | S2 | https://new.express.adobe.com/explore/templates | no-vision | nvda | B4 | T1 | reviewer (D. Fontaine), NVDA 2026.1.1 + Chrome 150.0.7871.187 |
| R014 | 2026-08-06 15:35 | S3 | https://new.express.adobe.com/id/urn:aaid:sc:US:1fd8af9a-87db-410e-8315-35fa3679dc86 | — | axe | — | — | — |
| R015 | 2026-08-06 15:46 | S3 | https://new.express.adobe.com/id/urn:aaid:sc:US:1fd8af9a-87db-410e-8315-35fa3679dc86 | no-vision | nvda | B4 | — | reviewer (D. Fontaine), NVDA 2026.1.1 + Chrome 150.0.7871.187 |
| R016 | 2026-08-06 16:49 | S3 | https://new.express.adobe.com/ (new blank document — ID recorded when created) | no-vision | nvda | B4 | T2 | reviewer (D. Fontaine), NVDA 2026.1.1 + Chrome 150.0.7871.187 |
| R017 | 2026-08-10 16:15 | S4 | https://new.express.adobe.com/your-stuff/files/recent?filter=express | — | axe | — | — | — |
| R018 | 2026-08-13 11:53 | S2 | https://new.express.adobe.com/explore/templates | low-vision | zoom | B3 | — | assistant (CDP 320px device emulation per testing-tools §zoom) |
| R019 | 2026-08-13 11:53 | S3 | https://new.express.adobe.com/id/urn:aaid:sc:US:1fd8af9a-87db-410e-8315-35fa3679dc86 | low-vision | zoom | B3 | — | assistant (CDP 320px device emulation) |
| R020 | 2026-08-13 11:53 | S4 | https://new.express.adobe.com/your-stuff/files/recent?filter=express | low-vision | zoom | B3 | — | assistant (CDP 320px device emulation) |
| R021 | 2026-08-13 12:22 | S2 | https://new.express.adobe.com/explore/templates | no-color | grayscale | — | — | assistant (CSS grayscale proxy per 03 s1.5) |
| R022 | 2026-08-13 12:22 | S3 | https://new.express.adobe.com/id/urn:aaid:sc:US:1fd8af9a-87db-410e-8315-35fa3679dc86 | no-color | grayscale | — | — | assistant (CSS grayscale proxy) |
| R023 | 2026-08-13 12:22 | S4 | https://new.express.adobe.com/your-stuff/files/recent?filter=express | no-color | grayscale | — | — | assistant (CSS grayscale proxy) |
| R024 | 2026-08-13 12:30 | S2 | https://new.express.adobe.com/explore/templates | no-hearing | inspection | — | — | assistant (DOM media audit, R021 O1) |
| R025 | 2026-08-13 12:30 | S2 | https://new.express.adobe.com/explore/templates | no-speech | inspection | — | — | assistant (inspection) |
| R026 | 2026-08-13 12:30 | S3 | https://new.express.adobe.com/id/urn:aaid:sc:US:1fd8af9a-87db-410e-8315-35fa3679dc86 | no-speech | inspection | — | — | assistant (inspection) |
| R027 | 2026-08-13 12:30 | S4 | https://new.express.adobe.com/your-stuff/files/recent?filter=express | no-hearing | inspection | — | — | assistant (DOM media audit, R023 O1) |
| R028 | 2026-08-13 12:30 | S4 | https://new.express.adobe.com/your-stuff/files/recent?filter=express | no-speech | inspection | — | — | assistant (inspection) |
| R029 | 2026-08-13 13:04 | S4 | https://new.express.adobe.com/your-stuff/files/recent?filter=express | no-vision | nvda | B4 | — | reviewer (D. Fontaine), NVDA 2026.1.1 + Chrome 150.0.7871.187 |
| R030 | 2026-08-13 13:48 | S3 | https://new.express.adobe.com/id/urn:aaid:sc:US:1fd8af9a-87db-410e-8315-35fa3679dc86 | no-hearing | inspection | — | — | reviewer (D. Fontaine) — video edit window capability inspection |
| R031 | 2026-08-13 14:28 | S3 | https://new.express.adobe.com/id/urn:aaid:sc:US:1fd8af9a-87db-410e-8315-35fa3679dc86 | motor | keyboard | B2 | — | reviewer (D. Fontaine), physical keyboard, NVDA off |
| R032 | 2026-08-13 15:21 | S2 | https://new.express.adobe.com/explore/templates | motor | keyboard | B2 | — | reviewer (D. Fontaine), physical keyboard, NVDA off |
| R033 | 2026-08-13 15:27 | S4 | https://new.express.adobe.com/your-stuff/files/recent?filter=express | motor | keyboard | B2 | — | reviewer (D. Fontaine), physical keyboard, NVDA off |
| R034 | 2026-08-13 15:43 | S2 | https://new.express.adobe.com/explore/templates | cognition | inspection | — | — | reviewer (D. Fontaine), cross-view closure |
| R035 | 2026-08-13 15:43 | S3 | https://new.express.adobe.com/id/urn:aaid:sc:US:1fd8af9a-87db-410e-8315-35fa3679dc86 | cognition | inspection | — | — | reviewer (D. Fontaine), cross-view closure |
| R036 | 2026-08-13 15:43 | S4 | https://new.express.adobe.com/your-stuff/files/recent?filter=express | cognition | inspection | — | — | reviewer (D. Fontaine), cross-view closure |
| R037 | 2026-08-14 11:30 | S3 | https://new.express.adobe.com/id/urn:aaid:sc:US:b1ab530f-f097-4a5f-8a6f-b8923fa65115 | no-vision | nvda | B4 | T2 | reviewer (D. Fontaine), NVDA 2026.1.1 + Chrome 151.0.7922.138 |
| R038 | 2026-08-14 12:39 | S3 | UI: Home -> new blank document -> three text objects 'text 1' / 'text 2' / 'text 3' (LOCATOR UNRESOLVED - /id/urn:aaid:sc:US:... to be pasted by reviewer, 2026-08-14) | no-vision | nvda | B4 | T2 | reviewer (D. Fontaine), NVDA 2026.1.1 |
| R039 | 2026-08-14 13:31 | Learn | https://new.express.adobe.com/learn | no-hearing | inspection | — | — | reviewer (D. Fontaine) - cursory pass |
| R040 | 2026-08-14 13:50 | S1 | 5-page sample across the app (exact page list to be confirmed); counter-example measured on S1 Home | — | wave | — | — | reviewer (D. Fontaine) |
| R041 | 2026-08-14 14:06 | S4 | UI: cross-cutting error-path probe across S1 Upload, S3 editor, S4 Your stuff (delete modal) and profile settings - session-error-paths-reviewer-walkthrough.md | — | inspection | — | — | reviewer (D. Fontaine) |
| R042 | 2026-08-14 14:14 | S1 | https://new.express.adobe.com/ - plus S2 /explore/templates, S3 /id/urn:aaid:sc:US:1fd8af9a-87db-410e-8315-35fa3679dc86, S4 /your-stuff/files/recent (four-view sweep) | — | inspection | — | — | assistant (CDP structural measurement, Chrome 151, extensions inert) |
