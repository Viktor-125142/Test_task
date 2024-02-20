query = """
WITH RankedSessions AS (
    SELECT
        c.communication_id,
        c.site_id,
        c.visitor_id,
        c.date_time AS communication_date_time,
        s.visitor_session_id,
        s.date_time AS session_date_time,
        s.campaign_id,
        ROW_NUMBER() OVER (PARTITION BY c.site_id, c.visitor_id ORDER BY s.date_time DESC) AS row_n
    FROM
        web_data.communications c
    LEFT JOIN
        web_data.sessions s ON c.site_id = s.site_id
                           AND c.visitor_id = s.visitor_id
                           AND s.date_time < c.date_time
)
SELECT
    communication_id,
    site_id,
    visitor_id,
    communication_date_time,
    visitor_session_id,
    session_date_time,
    campaign_id,
    COALESCE(row_n, 1) AS row_n
FROM
    RankedSessions
ORDER BY
    communication_id;

"""
