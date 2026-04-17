#!/usr/bin/env python3
"""
Test suite for aidev package
Tests basic functionality and imports
"""

import sys
import subprocess
import os
import json
from pathlib import Path

# Setup test config before imports
HOME = os.path.expanduser("~")
CONFIG_PATH = Path(HOME) / ".aidev" / "config.json"
CONFIG_PATH.parent.mkdir(parents=True, exist_ok=True)

# Create test config if it doesn't exist
if not CONFIG_PATH.exists():
    test_config = {
        "api_key": "sk-test-key-for-testing",
        "threshold": 0.3,
        "engine": "gpt-3.5-turbo",
        "length": 4096,
        "language": "en"
    }
    with open(CONFIG_PATH, 'w') as f:
        json.dump(test_config, f)
    print(f"✅ Test config created at {CONFIG_PATH}")

def test_imports():
    """Test that all modules can be imported"""
    print("🧪 Testing imports...")
    try:
        from aidev.config_utils import read_config, store_config
        from aidev.config_manager import manage_config
        print("✅ Config imports successful")
        return True
    except Exception as e:
        print(f"❌ Import error: {e}")
        return False

def test_cli_help():
    """Test CLI help command"""
    print("\n🧪 Testing CLI help...")
    try:
        result = subprocess.run(['aidev', '--help'], capture_output=True, text=True, timeout=5)
        if result.returncode == 0 and 'Usage:' in result.stdout:
            print("✅ CLI help works")
            print(f"   {result.stdout.split(chr(10))[0]}")
            return True
        else:
            print(f"❌ CLI help failed: {result.stderr}")
            return False
    except Exception as e:
        print(f"❌ CLI test error: {e}")
        return False

def test_config_command():
    """Test config manager"""
    print("\n🧪 Testing config command...")
    try:
        result = subprocess.run(['aidev-config', '--help'], capture_output=True, text=True, timeout=5)
        if result.returncode == 0 and 'Usage:' in result.stdout:
            print("✅ Config command works")
            return True
        else:
            print(f"❌ Config command failed: {result.stderr}")
            return False
    except Exception as e:
        print(f"❌ Config test error: {e}")
        return False

def test_version():
    """Test package version"""
    print("\n🧪 Testing version info...")
    try:
        from importlib.metadata import version
        pkg_version = version("aidev")
        print(f"✅ aidev version: {pkg_version}")
        return True
    except Exception as e:
        print(f"❌ Version check failed: {e}")
        return False

def run_all_tests():
    """Run all tests"""
    print("=" * 50)
    print("🎮 AIDEV TEST SUITE")
    print("=" * 50)
    
    tests = [
        test_version,
        test_imports,
        test_cli_help,
        test_config_command,
    ]
    
    results = []
    for test in tests:
        try:
            results.append(test())
        except Exception as e:
            print(f"❌ Unexpected error in {test.__name__}: {e}")
            results.append(False)
    
    print("\n" + "=" * 50)
    passed = sum(results)
    total = len(results)
    print(f"📊 Results: {passed}/{total} tests passed")
    print("=" * 50)
    
    return all(results)

if __name__ == "__main__":
    success = run_all_tests()
    sys.exit(0 if success else 1)
