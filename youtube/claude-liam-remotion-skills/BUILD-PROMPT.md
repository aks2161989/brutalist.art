# BUILD-PROMPT
> deep-explainer of the installed Remotion agent skills, Liam persona, into brutalist.art/youtube/claude-liam-remotion-skills/ (toolkit meta-series).
```bash
R=brutalist.art/youtube/claude-liam-remotion-skills
python3 $R/make_sheet.py
python3 brutalist.art/runtime/scripts/remotion_scenes.py $R
./brutalist.art/art run $R --height 2160
./brutalist.art/art final $R --height 2160 --out $R/exports/landscape
python3 brutalist.art/runtime/scripts/bookend_check.py $R
```
