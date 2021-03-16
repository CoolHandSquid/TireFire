import pandas as pd
import pandasql

def get_display_ttl():
    df      = pd.read_csv('TTL.csv')
    q       = "SELECT * FROM df"
    items   = pandasql.sqldf(q, locals())
    return items

def get_display_main():
    Main    = pd.read_csv('Main.csv')
    q       ="SELECT Name, Port, Description from Main GROUP BY Name ORDER By CASE WHEN Port LIKE '[0-9]%' THEN 2 ELSE 1 END, abs(Port)"
    #q       ="SELECT Name, Port, Description from Main GROUP BY Name ORDER By ABS(Port)"
    items   = pandasql.sqldf(q, locals())
    items   = items.values.tolist()
    return items

def get_display_sub(proto):
    Main    = pd.read_csv('Main.csv')
#    q       = "SELECT Cmd_Name, SUBSTRING(Cmd_Description, 1, 50), SUBSTRING(replace(Cmd_Command, X'0A', ' '), 1, 50) AS Cmd_Command from Main WHERE Name = '{}'".format(proto)
    q       = "SELECT Cmd_Name, SUBSTRING(Cmd_Description, 1, 50), SUBSTRING(replace(Cmd_Command, X'0A', ' '), 1, 50) AS Cmd_Command from Main WHERE Name = '{}' ORDER By SubDisplayOrder".format(proto)
#    q   = "SELECT Cmd_Name FROM Main WHERE Name = '{}'".format(proto)
    items   = pandasql.sqldf(q, locals())
    items   = items.values.tolist()
    return items

def get_fullcommand(proto):
    Main    = pd.read_csv('Main.csv')
    q       = "SELECT Cmd_Command from Main WHERE Name = '{}' ORDER By SubDisplayOrder".format(proto)
    items   = pandasql.sqldf(q, locals())
    items   = items.values.tolist()
    return items
