
select msisdn,domain, ET_Star_second as durations,1 as fdr_count,kbps,
       case when kbps >200 then 1 else 0 end isVideo,
       case when kbps <=200 then 1 else 0 end isAudio
       from (
                  select tt.starttime,
                         tt.endtime,
                         tt.et,
                         tt.ET_Star,
                         TIMESTAMPDIFF(SECOND, tt.starttime, tt.ET_Star) as ET_Star_second,
                         tt.msisdn,
                         tt.ulvolume,
                         tt.dlvolume,
                         tt.domain,
                         (ulvolume+dlvolume)/1024 as kbps
                  from (
                           select i.starttime,
                                  i.endtime,
                                  (i.endtime - INTERVAL 10 MINUTE) as et,
                                  CASE
                                      WHEN (i.endtime - INTERVAL 10 MINUTE) < i.starttime THEN i.endtime
                                      ELSE (i.endtime - INTERVAL 10 MINUTE)
                                      END                          as ET_Star,
                                  i.msisdn,
                                  i.ulvolume,
                                  i.dlvolume,
                                  i.domain
                           from ipdr i
                       ) as tt
              ) b  where kbps >=10