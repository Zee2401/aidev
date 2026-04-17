---
name: build-helper
description: "Use when: building projects, automating builds, setting up deployment pipelines, handling build errors, or optimizing build performance. Covers Python builds, EAS mobile builds, web builds, and cross-platform compilation."
applyTo: "**/*.py,**/package.json,**/*.toml,**/eas.json,**/setup.py"
---

# Build Helper

Assists with all build-related tasks across your projects.

## Quick Build Commands

**Python Package Build**:
```bash
pip install -e .  # development install
python setup.py build  # create distribution
```

**Mobile Builds (EAS)**:
```bash
eas build --platform android
eas build --platform ios
eas build --platform all  # both platforms
```

**Development Server**:
```bash
python -m http.server 8000  # web games
npm start  # node-based games
```

## Build Troubleshooting

When builds fail:
1. Check dependencies are installed: `pip list` or `npm list`
2. Verify environment setup (Python version, Node version)
3. Clear build cache: `rm -rf build/ dist/` (Python) or `rm -rf .expo/`
4. Review error logs for platform-specific issues
5. Test builds incrementally before full deployment

## Platform-Specific Tips

**Python**: Ensure setup.py is up-to-date, dependencies are pinned correctly
**Mobile (EAS)**: Check app.json config, verify API keys and certificates
**Web**: Monitor bundle size, optimize assets for browser loading

---

Use this helper whenever you need to build, deploy, or troubleshoot your projects!
