from arbitrage.core.datastructure.datetime import DateTime, EpochTimestampType, Tenor, TenorType, generate_datetime_sequence


start_datetime = DateTime(1625097600, EpochTimestampType.SECONDS)
end_datetime = DateTime(1656633600, EpochTimestampType.SECONDS)

seq = generate_datetime_sequence(start_datetime,end_datetime,Tenor(1,TenorType.MONTHS),False,False, True)

[s.get_date_in_string("%Y-%m-%d %H:%M:%S") for s in seq]

