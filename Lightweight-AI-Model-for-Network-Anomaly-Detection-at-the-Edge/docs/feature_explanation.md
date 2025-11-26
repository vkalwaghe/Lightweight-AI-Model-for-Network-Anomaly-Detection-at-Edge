# Feature explanation — micro-flow (1s windows)

This document explains the feature set used by the lightweight IDS prototype.  
Each row/window represents a 1-second micro-flow (or short-time window) aggregated from raw packets.

## Feature list

1. **packet_rate**
   - Units: packets / second
   - What: number of packets observed in the window.
   - Why useful: DDoS floods create extremely high packet rates compared to benign traffic.

2. **avg_pkt_size**
   - Units: bytes
   - What: mean packet size in the window.
   - Why useful: Many DDoS attacks use small packets (e.g. ping floods, SYN flood). Conversely, some application traffic has larger average sizes.

3. **std_pkt_size**
   - Units: bytes
   - What: standard deviation of packet sizes in the window.
   - Why useful: Port scans and some spoofing produce highly variable packet sizes; stable application flows have lower variance.

4. **dst_port_count**
   - Units: count
   - What: number of distinct destination ports observed in the window.
   - Why useful: Port scans target many destination ports in a short time; normal traffic targets few.

5. **tcp_flag_ratio**
   - Units: ratio (0..1)
   - What: fraction of packets in the window that are TCP (or have TCP flags set).
   - Why useful: Some attacks exploit TCP (SYN floods) while others (UDP floods) do not — looks at protocol mix.

6. **inter_arrival_mean**
   - Units: seconds
   - What: mean inter-packet arrival time (average time delta between consecutive packets).
   - Why useful: DDoS traffic tends to have very small inter-arrival times; benign traffic has higher, more varied inter-arrival times.

## Design principles
- **Lightweight:** compute only simple statistics; avoids payload parsing to reduce CPU/memory and privacy concerns.
- **Real-time friendly:** all features are O(n) per window and easy to maintain incrementally in a streaming setting.
- **Explainable:** features are directly interpretable — helps debugging false positives.

## How features are extracted (implementation notes)
- Windows are created using a fixed time window (default 1s). Packets are assigned to windows by timestamp.
- For `dst_port_count`, only TCP/UDP packets are considered (packets without a layer are ignored for port counting).
- For `inter_arrival_mean`, if a window contains 0 or 1 packet, the value is set to `0.0` (or clamped minimally).
- Feature values are clipped to a small positive lower bound before scaling to avoid numerical issues (e.g., `clip(lower=1e-4)`).

## How to extend
- Add features such as `unique_src_count`, `src_port_entropy`, `avg_window_packet_rate_change` for improved detection of distributed or stealthy attacks.
- Use rolling windows (overlap) to increase sensitivity for short bursts.
