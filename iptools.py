"""Offline IP inspection and list formatting helpers."""

from __future__ import annotations

import ipaddress


def inspect_ip(value: str) -> dict[str, str | bool | int]:
    address = ipaddress.ip_address(value.strip())
    return {
        "address": str(address),
        "version": address.version,
        "private": address.is_private,
        "global": address.is_global,
        "loopback": address.is_loopback,
        "multicast": address.is_multicast,
        "reserved": address.is_reserved,
    }


def format_ips(lines: list[str], template: str) -> list[str]:
    if "{ip}" not in template:
        raise ValueError("Template must contain {ip}.")
    output = []
    for line_number, raw in enumerate(lines, 1):
        value = raw.strip()
        if not value or value.startswith("#"):
            continue
        try:
            address = str(ipaddress.ip_address(value))
        except ValueError as exc:
            raise ValueError(f"Invalid IP address on line {line_number}.") from exc
        output.append(template.replace("{ip}", address))
    return output
