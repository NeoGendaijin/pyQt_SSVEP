#!/usr/bin/env python3
"""
Example usage of the SSVEP Visual Stimulator

This script demonstrates how to launch the SSVEP stimulator application
and provides examples of typical frequency settings for different experiments.
"""

from ssvep_stimulator import main

# Common SSVEP frequency combinations for different applications:

# BCI Classification (Binary):
# - Left: 10 Hz (Alpha band)
# - Right: 15 Hz (Beta band)

# BCI Classification (Multi-class):
# - Stimulus 1: 8 Hz
# - Stimulus 2: 10 Hz  
# - Stimulus 3: 12 Hz
# - Stimulus 4: 15 Hz

# Attention Studies:
# - Low attention: 6-8 Hz
# - High attention: 12-15 Hz

# Cognitive Load Assessment:
# - Low load: 8-10 Hz
# - High load: 15-20 Hz

if __name__ == "__main__":
    print("Starting SSVEP Visual Stimulator...")
    print("\nRecommended frequency combinations:")
    print("• Binary BCI: 10 Hz (left) + 15 Hz (right)")
    print("• Multi-class BCI: 8, 10, 12, 15 Hz")
    print("• Attention studies: 6-8 Hz vs 12-15 Hz")
    print("• Cognitive load: 8-10 Hz vs 15-20 Hz")
    print("\nLaunching application...")
    
    main()
