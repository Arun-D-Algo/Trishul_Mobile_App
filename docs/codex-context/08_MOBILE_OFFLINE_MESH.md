# Flutter Mobile, Offline Mode and Mesh/SOS

## Local storage
Use SQLite where practical. Cache:
- risk snapshots
- map metadata/demo geometry
- shelters
- emergency contacts
- route data
- pending reports/SOS
- synchronization status

## Offline flow
```text
ONLINE -> cache critical region -> NETWORK LOST
       -> read cache -> create local report/SOS -> queue
       -> NETWORK RESTORED -> sync idempotently
```

Each event should have a UUID, timestamp, event type, location, payload, sync status and retry count.

## Connectivity
Show clear online/offline state. Offline operation must not silently display stale data as live; show last-updated time.

## BLE/peer-to-peer
Define a transport abstraction. A deterministic simulated peer transport is acceptable for the SIH MVP. Real BLE/Wi-Fi Direct should be added only after the end-to-end product is stable.
