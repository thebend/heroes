# Return a function that does nothing by default
def default_processor(player, event):
    pass

processors = {}
def get(id):
    try: return processors[id]
    except KeyError: return default_processor

def TrackerProcessor(id):
    def set_processor(processor):
        processors[id] = processor
        return processor
    return set_processor

# event IDs 3 and 8 might be useful?
tracker_ids = {
    0: (183, 'SPlayerStatsEvent'), # confirmed irrelevant
    # can detect spawning of minions and spell-based units
    # should find a more universal way to detect spell casting
    1: (184, 'SUnitBornEvent'),
    2: (185, 'SUnitDiedEvent'), # useful
    3: (186, 'SUnitOwnerChangeEvent'),
    # used when towers change to dead versions while stuck to gate
    # might be useful but should have universal way of finding building death
    4: (187, 'SUnitTypeChangeEvent'),
    5: (188, 'SUpgradeEvent'), # confirmed irrelevant
    6: (184, 'SUnitInitEvent'), # not used
    7: (189, 'SUnitDoneEvent'), # not used
    8: (191, 'SUnitPositionsEvent'),
    9: (192, 'SPlayerSetupEvent') # confirmed irrelevant
}
