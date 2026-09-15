#!/usr/bin/env python
# -*- coding: utf-8 -*-

"""
Application de gestion du prix Goncourt 2026
"""

from business.goncourt import Goncourt


def main() -> None:
    """Programme principal."""
    print("--------------------------    "
          "Prix Goncourt 2026    "
          "--------------------------""")

    goncourt_instance: Goncourt = Goncourt()





if __name__ == '__main__':
    main()
