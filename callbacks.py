import plotly.express as px
from dash.dependencies import Input, Output, State
from datetime import datetime as dt
from dateutil import relativedelta
from app import app
from data import sale, humanizer, growthStr
import pandas as pd

# Callbacks for all cards
# Sale, Txn & APC

@app.callback([Output('total-sale','children'),
              Output('total-trans','children'),
              Output('total-apc','children'),
              Output('total-last-day-sale','children')],
              [Input('submit-btn','n_clicks')],
              [State('dropD1','value'),
                State('dropDBrand','value'),
                State('datePicker','start_date'),
                State('datePicker','end_date')])
def sale_filtering(n_clicks,dropValue,dropValueBrand,startdate,enddate):
    if (dropValue == "All City") & (dropValueBrand == "All Brand"):
        sale_filtered = sale[(sale['Trans Date'] >= pd.to_datetime(startdate)) & (sale['Trans Date'] <= pd.to_datetime(enddate))].copy()
        
        lastDay = enddate

        totalSales = sale_filtered['NetAmount'].sum().round()
        totalTrans = sale_filtered['Txn'].sum().round()
        apc = (totalSales/totalTrans).round(2)
        lastDaySale = sale_filtered[sale_filtered['Trans Date'] == lastDay]['NetAmount'].sum().round()
        
        return humanizer(totalSales),humanizer(totalTrans), apc, humanizer(lastDaySale)
    elif (dropValue == "All City") & (dropValueBrand != "All Brand"):
        if dropValueBrand == "Wow! Momo":
            sale_filter =sale[(sale['Trans Date'] >= pd.to_datetime(startdate)) & (sale['Trans Date'] <= pd.to_datetime(enddate))].copy()
            
            sale_filtered = sale_filter[sale_filter['Brand']==dropValueBrand]

            lastDay = enddate

            totalSales = sale_filtered['NetAmount'].sum().round()
            totalTrans = sale_filtered['Txn'].sum().round()
            apc = (totalSales/totalTrans).round(2)
            lastDaySaleFilter = sale[sale['Trans Date'] == lastDay]
            lastDaySale = lastDaySaleFilter[lastDaySaleFilter['Brand']==dropValueBrand]['NetAmount'].sum().round()
            return humanizer(totalSales),humanizer(totalTrans), apc, humanizer(lastDaySale)
        elif dropValueBrand == "Wow! China":
            sale_filter =sale[(sale['Trans Date'] >= pd.to_datetime(startdate)) & (sale['Trans Date'] <= pd.to_datetime(enddate))].copy()
            
            sale_filtered = sale_filter[sale_filter['Brand']==dropValueBrand]

            lastDay = enddate

            totalSales = sale_filtered['NetAmount'].sum().round()
            totalTrans = sale_filtered['Txn'].sum().round()
            apc = (totalSales/totalTrans).round(2)
            lastDaySaleFilter = sale[sale['Trans Date'] == lastDay]
            lastDaySale = lastDaySaleFilter[lastDaySaleFilter['Brand']==dropValueBrand]['NetAmount'].sum().round()
            return humanizer(totalSales),humanizer(totalTrans), apc, humanizer(lastDaySale)
        elif dropValueBrand == "Combo":
            sale_filter =sale[(sale['Trans Date'] >= pd.to_datetime(startdate)) & (sale['Trans Date'] <= pd.to_datetime(enddate))].copy()
            
            sale_filtered = sale_filter[sale_filter['Brand']==dropValueBrand]

            lastDay = enddate

            totalSales = sale_filtered['NetAmount'].sum().round()
            totalTrans = sale_filtered['Txn'].sum().round()
            apc = (totalSales/totalTrans).round(2)
            lastDaySaleFilter = sale[sale['Trans Date'] == lastDay]
            lastDaySale = lastDaySaleFilter[lastDaySaleFilter['Brand']==dropValueBrand]['NetAmount'].sum().round()
            return humanizer(totalSales),humanizer(totalTrans), apc, humanizer(lastDaySale)
        else:
            sale_filter =sale[(sale['Trans Date'] >= pd.to_datetime(startdate)) & (sale['Trans Date'] <= pd.to_datetime(enddate))].copy()
            
            sale_filtered = sale_filter[sale_filter['City']==dropValue]

            lastDay = enddate

            totalSales = sale_filtered['NetAmount'].sum().round()
            totalTrans = sale_filtered['Txn'].sum().round()
            apc = (totalSales/totalTrans).round(2)
            lastDaySaleFilter = sale[sale['Trans Date'] == lastDay]
            lastDaySale = lastDaySaleFilter[lastDaySaleFilter['City']==dropValue]['NetAmount'].sum().round()
            return humanizer(totalSales),humanizer(totalTrans), apc, humanizer(lastDaySale)

    else:
        if dropValueBrand == "Wow! Momo":
            sale_filter =sale[(sale['Trans Date'] >= pd.to_datetime(startdate)) & (sale['Trans Date'] <= pd.to_datetime(enddate))].copy()
            
            sale_filtered = sale_filter[(sale_filter['City']==dropValue) & (sale_filter['Brand']==dropValueBrand)]

            lastDay = enddate

            totalSales = sale_filtered['NetAmount'].sum().round()
            totalTrans = sale_filtered['Txn'].sum().round()
            apc = (totalSales/totalTrans).round(2)
            lastDaySaleFilter = sale[sale['Trans Date'] == lastDay]
            lastDaySale = lastDaySaleFilter[(lastDaySaleFilter['City']==dropValue) & (lastDaySaleFilter['Brand']==dropValueBrand)]['NetAmount'].sum().round()
            return humanizer(totalSales),humanizer(totalTrans), apc, humanizer(lastDaySale)
        elif dropValueBrand == "Wow! China":
            sale_filter =sale[(sale['Trans Date'] >= pd.to_datetime(startdate)) & (sale['Trans Date'] <= pd.to_datetime(enddate))].copy()
            
            sale_filtered = sale_filter[(sale_filter['City']==dropValue) & (sale_filter['Brand']==dropValueBrand)]

            lastDay = enddate

            totalSales = sale_filtered['NetAmount'].sum().round()
            totalTrans = sale_filtered['Txn'].sum().round()
            apc = (totalSales/totalTrans).round(2)
            lastDaySaleFilter = sale[sale['Trans Date'] == lastDay]
            lastDaySale = lastDaySaleFilter[(lastDaySaleFilter['City']==dropValue) & (lastDaySaleFilter['Brand']==dropValueBrand)]['NetAmount'].sum().round()
            return humanizer(totalSales),humanizer(totalTrans), apc, humanizer(lastDaySale)
        elif dropValueBrand == "Combo":
            sale_filter =sale[(sale['Trans Date'] >= pd.to_datetime(startdate)) & (sale['Trans Date'] <= pd.to_datetime(enddate))].copy()
            
            sale_filtered = sale_filter[(sale_filter['City']==dropValue) & (sale_filter['Brand']==dropValueBrand)]

            lastDay = enddate

            totalSales = sale_filtered['NetAmount'].sum().round()
            totalTrans = sale_filtered['Txn'].sum().round()
            apc = (totalSales/totalTrans).round(2)
            lastDaySaleFilter = sale[sale['Trans Date'] == lastDay]
            lastDaySale = lastDaySaleFilter[(lastDaySaleFilter['City']==dropValue) & (lastDaySaleFilter['Brand']==dropValueBrand)]['NetAmount'].sum().round()
            return humanizer(totalSales),humanizer(totalTrans), apc, humanizer(lastDaySale)
        else:
            sale_filter =sale[(sale['Trans Date'] >= pd.to_datetime(startdate)) & (sale['Trans Date'] <= pd.to_datetime(enddate))].copy()
            
            sale_filtered = sale_filter[sale_filter['City']==dropValue]

            lastDay = enddate

            totalSales = sale_filtered['NetAmount'].sum().round()
            totalTrans = sale_filtered['Txn'].sum().round()
            apc = (totalSales/totalTrans).round(2)
            lastDaySaleFilter = sale[sale['Trans Date'] == lastDay]
            lastDaySale = lastDaySaleFilter[lastDaySaleFilter['City']==dropValue]['NetAmount'].sum().round()
            return humanizer(totalSales),humanizer(totalTrans), apc, humanizer(lastDaySale)

# Card growth, de-growth

@app.callback([Output('total-sale-gd','children'),
              Output('total-trans-gd','children'),  
              Output('total-apc-gd','children'),
              Output('total-last-day-sale-gd','children')],
              [Input('submit-btn','n_clicks')],
              [State('dropD1','value'),
                State('dropDBrand','value'),
                State('datePicker','start_date'),
                State('datePicker','end_date')])
def sale_filtering(n_clicks,dropValue,dropValueBrand,startdate,enddate):
    if (dropValue == "All City") & (dropValueBrand == "All Brand"):
        # This month's sales
        sale_filtered = sale[(sale['Trans Date'] >= pd.to_datetime(startdate)) & (sale['Trans Date'] <= pd.to_datetime(enddate))].copy()
        
        lastDay = enddate

        totalSales = sale_filtered['NetAmount'].sum().round()
        totalTrans = sale_filtered['Txn'].sum().round()
        apc = (totalSales/totalTrans).round(2)
        lastDaySale = sale_filtered[sale_filtered['Trans Date'] == lastDay]['NetAmount'].sum().round()

        # Last Month's Sales
        lmStartDate = pd.to_datetime(startdate) + relativedelta.relativedelta(months=-1)
        lmEndDate = pd.to_datetime(enddate) + relativedelta.relativedelta(months=-1)
        LastWeekSameDay = pd.to_datetime(enddate) + relativedelta.relativedelta(days=-7)

        lm_sale_filtered = sale[(sale['Trans Date'] >= lmStartDate) & (sale['Trans Date'] <= lmEndDate)].copy()
        

        lmTotalSales = lm_sale_filtered['NetAmount'].sum().round()
        lmTotalTrans = lm_sale_filtered['Txn'].sum().round()
        lmApc = (lmTotalSales/lmTotalTrans).round(2)
        LastWeekSameDaySale = sale[sale['Trans Date'] == LastWeekSameDay]['NetAmount'].sum().round()

        return growthStr(totalSales,lmTotalSales, "month"), growthStr(totalTrans,lmTotalTrans, "month"), growthStr(apc,lmApc,"month"), growthStr(lastDaySale,LastWeekSameDaySale,"week")

    elif (dropValue == "All City") & (dropValueBrand != "All Brand"):
        if dropValueBrand == "Wow! Momo":
            # This month's sales
            sale_filter = sale[(sale['Trans Date'] >= pd.to_datetime(startdate)) & (sale['Trans Date'] <= pd.to_datetime(enddate))].copy()
            
            sale_filtered = sale_filter[sale_filter['Brand'] == dropValueBrand]

            lastDay = enddate

            totalSales = sale_filtered['NetAmount'].sum().round()
            totalTrans = sale_filtered['Txn'].sum().round()
            apc = (totalSales/totalTrans).round(2)
            lastDaySaleFilter = sale[sale['Trans Date'] == lastDay]
            lastDaySale = lastDaySaleFilter[lastDaySaleFilter['Brand'] == dropValueBrand]['NetAmount'].sum().round()

            # Last Month's Sales
            lmStartDate = pd.to_datetime(startdate) + relativedelta.relativedelta(months=-1)
            lmEndDate = pd.to_datetime(enddate) + relativedelta.relativedelta(months=-1)
            LastWeekSameDay = pd.to_datetime(enddate) + relativedelta.relativedelta(days=-7)

            lm_sale_filter = sale[(sale['Trans Date'] >= lmStartDate) & (sale['Trans Date'] <= lmEndDate)].copy()
            
            lm_sale_filtered = lm_sale_filter[lm_sale_filter['Brand'] == dropValueBrand]

            lmTotalSales = lm_sale_filtered['NetAmount'].sum().round()
            lmTotalTrans = lm_sale_filtered['Txn'].sum().round()
            lmApc = (lmTotalSales/lmTotalTrans).round(2)
            LastWeekSameDaySaleFilter = sale[sale['Trans Date'] == LastWeekSameDay]
            LastWeekSameDaySale = LastWeekSameDaySaleFilter[LastWeekSameDaySaleFilter['Brand'] == dropValueBrand]['NetAmount'].sum().round()

            return growthStr(totalSales,lmTotalSales, "month"), growthStr(totalTrans,lmTotalTrans, "month"), growthStr(apc,lmApc,"month"), growthStr(lastDaySale,LastWeekSameDaySale,"week")
        elif dropValueBrand == "Wow! China":
            # This month's sales
            sale_filter = sale[(sale['Trans Date'] >= pd.to_datetime(startdate)) & (sale['Trans Date'] <= pd.to_datetime(enddate))].copy()
            
            sale_filtered = sale_filter[sale_filter['Brand'] == dropValueBrand]

            lastDay = enddate

            totalSales = sale_filtered['NetAmount'].sum().round()
            totalTrans = sale_filtered['Txn'].sum().round()
            apc = (totalSales/totalTrans).round(2)
            lastDaySaleFilter = sale[sale['Trans Date'] == lastDay]
            lastDaySale = lastDaySaleFilter[lastDaySaleFilter['Brand'] == dropValueBrand]['NetAmount'].sum().round()

            # Last Month's Sales
            lmStartDate = pd.to_datetime(startdate) + relativedelta.relativedelta(months=-1)
            lmEndDate = pd.to_datetime(enddate) + relativedelta.relativedelta(months=-1)
            LastWeekSameDay = pd.to_datetime(enddate) + relativedelta.relativedelta(days=-7)

            lm_sale_filter = sale[(sale['Trans Date'] >= lmStartDate) & (sale['Trans Date'] <= lmEndDate)].copy()
            
            lm_sale_filtered = lm_sale_filter[lm_sale_filter['Brand'] == dropValueBrand]

            lmTotalSales = lm_sale_filtered['NetAmount'].sum().round()
            lmTotalTrans = lm_sale_filtered['Txn'].sum().round()
            lmApc = (lmTotalSales/lmTotalTrans).round(2)
            LastWeekSameDaySaleFilter = sale[sale['Trans Date'] == LastWeekSameDay]
            LastWeekSameDaySale = LastWeekSameDaySaleFilter[LastWeekSameDaySaleFilter['Brand'] == dropValueBrand]['NetAmount'].sum().round()

            return growthStr(totalSales,lmTotalSales, "month"), growthStr(totalTrans,lmTotalTrans, "month"), growthStr(apc,lmApc,"month"), growthStr(lastDaySale,LastWeekSameDaySale,"week")
        elif dropValueBrand == "Combo":
            # This month's sales
            sale_filter = sale[(sale['Trans Date'] >= pd.to_datetime(startdate)) & (sale['Trans Date'] <= pd.to_datetime(enddate))].copy()
            
            sale_filtered = sale_filter[sale_filter['Brand'] == dropValueBrand]

            lastDay = enddate

            totalSales = sale_filtered['NetAmount'].sum().round()
            totalTrans = sale_filtered['Txn'].sum().round()
            apc = (totalSales/totalTrans).round(2)
            lastDaySaleFilter = sale[sale['Trans Date'] == lastDay]
            lastDaySale = lastDaySaleFilter[lastDaySaleFilter['Brand'] == dropValueBrand]['NetAmount'].sum().round()

            # Last Month's Sales
            lmStartDate = pd.to_datetime(startdate) + relativedelta.relativedelta(months=-1)
            lmEndDate = pd.to_datetime(enddate) + relativedelta.relativedelta(months=-1)
            LastWeekSameDay = pd.to_datetime(enddate) + relativedelta.relativedelta(days=-7)

            lm_sale_filter = sale[(sale['Trans Date'] >= lmStartDate) & (sale['Trans Date'] <= lmEndDate)].copy()
            
            lm_sale_filtered = lm_sale_filter[lm_sale_filter['Brand'] == dropValueBrand]

            lmTotalSales = lm_sale_filtered['NetAmount'].sum().round()
            lmTotalTrans = lm_sale_filtered['Txn'].sum().round()
            lmApc = (lmTotalSales/lmTotalTrans).round(2)
            LastWeekSameDaySaleFilter = sale[sale['Trans Date'] == LastWeekSameDay]
            LastWeekSameDaySale = LastWeekSameDaySaleFilter[LastWeekSameDaySaleFilter['Brand'] == dropValueBrand]['NetAmount'].sum().round()

            return growthStr(totalSales,lmTotalSales, "month"), growthStr(totalTrans,lmTotalTrans, "month"), growthStr(apc,lmApc,"month"), growthStr(lastDaySale,LastWeekSameDaySale,"week")
        else:
            # This month's sales
            sale_filter = sale[(sale['Trans Date'] >= pd.to_datetime(startdate)) & (sale['Trans Date'] <= pd.to_datetime(enddate))].copy()
            
            sale_filtered = sale_filter[sale_filter['City'] == dropValue]

            lastDay = enddate

            totalSales = sale_filtered['NetAmount'].sum().round()
            totalTrans = sale_filtered['Txn'].sum().round()
            apc = (totalSales/totalTrans).round(2)
            lastDaySaleFilter = sale[sale['Trans Date'] == lastDay]
            lastDaySale = lastDaySaleFilter[lastDaySaleFilter['City'] == dropValue]['NetAmount'].sum().round()

            # Last Month's Sales
            lmStartDate = pd.to_datetime(startdate) + relativedelta.relativedelta(months=-1)
            lmEndDate = pd.to_datetime(enddate) + relativedelta.relativedelta(months=-1)
            LastWeekSameDay = pd.to_datetime(enddate) + relativedelta.relativedelta(days=-7)

            lm_sale_filter = sale[(sale['Trans Date'] >= lmStartDate) & (sale['Trans Date'] <= lmEndDate)].copy()
            
            lm_sale_filtered = lm_sale_filter[lm_sale_filter['City'] == dropValue]

            lmTotalSales = lm_sale_filtered['NetAmount'].sum().round()
            lmTotalTrans = lm_sale_filtered['Txn'].sum().round()
            lmApc = (lmTotalSales/lmTotalTrans).round(2)
            LastWeekSameDaySaleFilter = sale[sale['Trans Date'] == LastWeekSameDay]
            LastWeekSameDaySale = LastWeekSameDaySaleFilter[LastWeekSameDaySaleFilter['City'] == dropValue]['NetAmount'].sum().round()

            return growthStr(totalSales,lmTotalSales, "month"), growthStr(totalTrans,lmTotalTrans, "month"), growthStr(apc,lmApc,"month"), growthStr(lastDaySale,LastWeekSameDaySale,"week")

    else:
        if dropValueBrand == "Wow! Momo":
            # This month's sales
            sale_filter = sale[(sale['Trans Date'] >= pd.to_datetime(startdate)) & (sale['Trans Date'] <= pd.to_datetime(enddate))].copy()
            
            sale_filtered = sale_filter[(sale_filter['City'] == dropValue) & (sale_filter['Brand'] == dropValueBrand)]

            lastDay = enddate

            totalSales = sale_filtered['NetAmount'].sum().round()
            totalTrans = sale_filtered['Txn'].sum().round()
            apc = (totalSales/totalTrans).round(2)
            lastDaySaleFilter = sale[sale['Trans Date'] == lastDay]
            lastDaySale = lastDaySaleFilter[(lastDaySaleFilter['City'] == dropValue) & (lastDaySaleFilter['Brand'] == dropValueBrand)]['NetAmount'].sum().round()

            # Last Month's Sales
            lmStartDate = pd.to_datetime(startdate) + relativedelta.relativedelta(months=-1)
            lmEndDate = pd.to_datetime(enddate) + relativedelta.relativedelta(months=-1)
            LastWeekSameDay = pd.to_datetime(enddate) + relativedelta.relativedelta(days=-7)

            lm_sale_filter = sale[(sale['Trans Date'] >= lmStartDate) & (sale['Trans Date'] <= lmEndDate)].copy()
            
            lm_sale_filtered = lm_sale_filter[(lm_sale_filter['City'] == dropValue) & (lm_sale_filter['Brand'] == dropValueBrand)]

            lmTotalSales = lm_sale_filtered['NetAmount'].sum().round()
            lmTotalTrans = lm_sale_filtered['Txn'].sum().round()
            lmApc = (lmTotalSales/lmTotalTrans).round(2)
            LastWeekSameDaySaleFilter = sale[sale['Trans Date'] == LastWeekSameDay]
            LastWeekSameDaySale = LastWeekSameDaySaleFilter[(LastWeekSameDaySaleFilter['City'] == dropValue) & (LastWeekSameDaySaleFilter['Brand'] == dropValueBrand)]['NetAmount'].sum().round()

            return growthStr(totalSales,lmTotalSales, "month"), growthStr(totalTrans,lmTotalTrans, "month"), growthStr(apc,lmApc,"month"), growthStr(lastDaySale,LastWeekSameDaySale,"week")
        elif dropValueBrand == "Wow! China":
            # This month's sales
            sale_filter = sale[(sale['Trans Date'] >= pd.to_datetime(startdate)) & (sale['Trans Date'] <= pd.to_datetime(enddate))].copy()
            
            sale_filtered = sale_filter[(sale_filter['City'] == dropValue) & (sale_filter['Brand'] == dropValueBrand)]

            lastDay = enddate

            totalSales = sale_filtered['NetAmount'].sum().round()
            totalTrans = sale_filtered['Txn'].sum().round()
            apc = (totalSales/totalTrans).round(2)
            lastDaySaleFilter = sale[sale['Trans Date'] == lastDay]
            lastDaySale = lastDaySaleFilter[(lastDaySaleFilter['City'] == dropValue) & (lastDaySaleFilter['Brand'] == dropValueBrand)]['NetAmount'].sum().round()

            # Last Month's Sales
            lmStartDate = pd.to_datetime(startdate) + relativedelta.relativedelta(months=-1)
            lmEndDate = pd.to_datetime(enddate) + relativedelta.relativedelta(months=-1)
            LastWeekSameDay = pd.to_datetime(enddate) + relativedelta.relativedelta(days=-7)

            lm_sale_filter = sale[(sale['Trans Date'] >= lmStartDate) & (sale['Trans Date'] <= lmEndDate)].copy()
            
            lm_sale_filtered = lm_sale_filter[(lm_sale_filter['City'] == dropValue) & (lm_sale_filter['Brand'] == dropValueBrand)]

            lmTotalSales = lm_sale_filtered['NetAmount'].sum().round()
            lmTotalTrans = lm_sale_filtered['Txn'].sum().round()
            lmApc = (lmTotalSales/lmTotalTrans).round(2)
            LastWeekSameDaySaleFilter = sale[sale['Trans Date'] == LastWeekSameDay]
            LastWeekSameDaySale = LastWeekSameDaySaleFilter[(LastWeekSameDaySaleFilter['City'] == dropValue) & (LastWeekSameDaySaleFilter['Brand'] == dropValueBrand)]['NetAmount'].sum().round()

            return growthStr(totalSales,lmTotalSales, "month"), growthStr(totalTrans,lmTotalTrans, "month"), growthStr(apc,lmApc,"month"), growthStr(lastDaySale,LastWeekSameDaySale,"week")
        elif dropValueBrand == "Combo":
            # This month's sales
            sale_filter = sale[(sale['Trans Date'] >= pd.to_datetime(startdate)) & (sale['Trans Date'] <= pd.to_datetime(enddate))].copy()
            
            sale_filtered = sale_filter[(sale_filter['City'] == dropValue) & (sale_filter['Brand'] == dropValueBrand)]

            lastDay = enddate

            totalSales = sale_filtered['NetAmount'].sum().round()
            totalTrans = sale_filtered['Txn'].sum().round()
            apc = (totalSales/totalTrans).round(2)
            lastDaySaleFilter = sale[sale['Trans Date'] == lastDay]
            lastDaySale = lastDaySaleFilter[(lastDaySaleFilter['City'] == dropValue) & (lastDaySaleFilter['Brand'] == dropValueBrand)]['NetAmount'].sum().round()

            # Last Month's Sales
            lmStartDate = pd.to_datetime(startdate) + relativedelta.relativedelta(months=-1)
            lmEndDate = pd.to_datetime(enddate) + relativedelta.relativedelta(months=-1)
            LastWeekSameDay = pd.to_datetime(enddate) + relativedelta.relativedelta(days=-7)

            lm_sale_filter = sale[(sale['Trans Date'] >= lmStartDate) & (sale['Trans Date'] <= lmEndDate)].copy()
            
            lm_sale_filtered = lm_sale_filter[(lm_sale_filter['City'] == dropValue) & (lm_sale_filter['Brand'] == dropValueBrand)]

            lmTotalSales = lm_sale_filtered['NetAmount'].sum().round()
            lmTotalTrans = lm_sale_filtered['Txn'].sum().round()
            lmApc = (lmTotalSales/lmTotalTrans).round(2)
            LastWeekSameDaySaleFilter = sale[sale['Trans Date'] == LastWeekSameDay]
            LastWeekSameDaySale = LastWeekSameDaySaleFilter[(LastWeekSameDaySaleFilter['City'] == dropValue) & (LastWeekSameDaySaleFilter['Brand'] == dropValueBrand)]['NetAmount'].sum().round()

            return growthStr(totalSales,lmTotalSales, "month"), growthStr(totalTrans,lmTotalTrans, "month"), growthStr(apc,lmApc,"month"), growthStr(lastDaySale,LastWeekSameDaySale,"week")
        else:
            # This month's sales
            sale_filter = sale[(sale['Trans Date'] >= pd.to_datetime(startdate)) & (sale['Trans Date'] <= pd.to_datetime(enddate))].copy()
            
            sale_filtered = sale_filter[(sale_filter['City'] == dropValue)]

            lastDay = enddate

            totalSales = sale_filtered['NetAmount'].sum().round()
            totalTrans = sale_filtered['Txn'].sum().round()
            apc = (totalSales/totalTrans).round(2)
            lastDaySaleFilter = sale[sale['Trans Date'] == lastDay]
            lastDaySale = lastDaySaleFilter[(lastDaySaleFilter['City'] == dropValue)]['NetAmount'].sum().round()

            # Last Month's Sales
            lmStartDate = pd.to_datetime(startdate) + relativedelta.relativedelta(months=-1)
            lmEndDate = pd.to_datetime(enddate) + relativedelta.relativedelta(months=-1)
            LastWeekSameDay = pd.to_datetime(enddate) + relativedelta.relativedelta(days=-7)

            lm_sale_filter = sale[(sale['Trans Date'] >= lmStartDate) & (sale['Trans Date'] <= lmEndDate)].copy()
            
            lm_sale_filtered = lm_sale_filter[(lm_sale_filter['City'] == dropValue)]

            lmTotalSales = lm_sale_filtered['NetAmount'].sum().round()
            lmTotalTrans = lm_sale_filtered['Txn'].sum().round()
            lmApc = (lmTotalSales/lmTotalTrans).round(2)
            LastWeekSameDaySaleFilter = sale[sale['Trans Date'] == LastWeekSameDay]
            LastWeekSameDaySale = LastWeekSameDaySaleFilter[(LastWeekSameDaySaleFilter['City'] == dropValue)]['NetAmount'].sum().round()

            return growthStr(totalSales,lmTotalSales, "month"), growthStr(totalTrans,lmTotalTrans, "month"), growthStr(apc,lmApc,"month"), growthStr(lastDaySale,LastWeekSameDaySale,"week")


# Last months sales figure

@app.callback([Output('total-sale-lm','children'),
              Output('total-trans-lm','children'),
              Output('total-apc-lm','children'),
              Output('total-last-day-sale-lw','children')],
              [Input('submit-btn','n_clicks')],
              [State('dropD1','value'),
                State('dropDBrand','value'),
                State('datePicker','start_date'),
                State('datePicker','end_date')])
def sale_filtering(n_clicks,dropValue,dropValueBrand,startdate,enddate):
    if (dropValue == "All City") & (dropValueBrand == "All Brand"):
        lmStartDate = pd.to_datetime(startdate) + relativedelta.relativedelta(months=-1)
        lmEndDate = pd.to_datetime(enddate) + relativedelta.relativedelta(months=-1)
        LastWeekSameDay = pd.to_datetime(enddate) + relativedelta.relativedelta(days=-7)

        lm_sale_filtered = sale[(sale['Trans Date'] >= lmStartDate) & (sale['Trans Date'] <= lmEndDate)].copy()
        

        lmTotalSales = lm_sale_filtered['NetAmount'].sum().round()
        lmTotalTrans = lm_sale_filtered['Txn'].sum().round()
        lmApc = (lmTotalSales/lmTotalTrans).round(2)
        LastWeekSameDaySale = sale[sale['Trans Date'] == LastWeekSameDay]['NetAmount'].sum().round()
        
        return f"Last month: {humanizer(lmTotalSales)}", f"Last month: {humanizer(lmTotalTrans)}",f"Last month: {humanizer(lmApc)}", f"Last week SD: {humanizer(LastWeekSameDaySale)}"
    
    elif (dropValue == "All City") & (dropValueBrand != "All Brand") :
        if dropValueBrand == "Wow! Momo":
            lmStartDate = pd.to_datetime(startdate) + relativedelta.relativedelta(months=-1)
            lmEndDate = pd.to_datetime(enddate) + relativedelta.relativedelta(months=-1)
            LastWeekSameDay = pd.to_datetime(enddate) + relativedelta.relativedelta(days=-7)

            lm_sale_filter = sale[(sale['Trans Date'] >= lmStartDate) & (sale['Trans Date'] <= lmEndDate)].copy()
            lm_sale_filtered = lm_sale_filter[lm_sale_filter['Brand'] == dropValueBrand]

            lmTotalSales = lm_sale_filtered['NetAmount'].sum().round()
            lmTotalTrans = lm_sale_filtered['Txn'].sum().round()
            lmApc = (lmTotalSales/lmTotalTrans).round(2)
            LastWeekSameDaySaleFilter = sale[sale['Trans Date'] == LastWeekSameDay]
            LastWeekSameDaySale = LastWeekSameDaySaleFilter[LastWeekSameDaySaleFilter['Brand'] == dropValueBrand]['NetAmount'].sum().round()

            return f"Last month: {humanizer(lmTotalSales)}", f"Last month: {humanizer(lmTotalTrans)}",f"Last month: {humanizer(lmApc)}", f"Last week SD: {humanizer(LastWeekSameDaySale)}"
        
        elif dropValueBrand == "Wow! China":
            lmStartDate = pd.to_datetime(startdate) + relativedelta.relativedelta(months=-1)
            lmEndDate = pd.to_datetime(enddate) + relativedelta.relativedelta(months=-1)
            LastWeekSameDay = pd.to_datetime(enddate) + relativedelta.relativedelta(days=-7)

            lm_sale_filter = sale[(sale['Trans Date'] >= lmStartDate) & (sale['Trans Date'] <= lmEndDate)].copy()
            lm_sale_filtered = lm_sale_filter[lm_sale_filter['Brand'] == dropValueBrand]

            lmTotalSales = lm_sale_filtered['NetAmount'].sum().round()
            lmTotalTrans = lm_sale_filtered['Txn'].sum().round()
            lmApc = (lmTotalSales/lmTotalTrans).round(2)
            LastWeekSameDaySaleFilter = sale[sale['Trans Date'] == LastWeekSameDay]
            LastWeekSameDaySale = LastWeekSameDaySaleFilter[LastWeekSameDaySaleFilter['Brand'] == dropValueBrand]['NetAmount'].sum().round()

            return f"Last month: {humanizer(lmTotalSales)}", f"Last month: {humanizer(lmTotalTrans)}",f"Last month: {humanizer(lmApc)}", f"Last week SD: {humanizer(LastWeekSameDaySale)}"
        
        elif dropValueBrand == "Combo":
            lmStartDate = pd.to_datetime(startdate) + relativedelta.relativedelta(months=-1)
            lmEndDate = pd.to_datetime(enddate) + relativedelta.relativedelta(months=-1)
            LastWeekSameDay = pd.to_datetime(enddate) + relativedelta.relativedelta(days=-7)

            lm_sale_filter = sale[(sale['Trans Date'] >= lmStartDate) & (sale['Trans Date'] <= lmEndDate)].copy()
            lm_sale_filtered = lm_sale_filter[lm_sale_filter['Brand'] == dropValueBrand]

            lmTotalSales = lm_sale_filtered['NetAmount'].sum().round()
            lmTotalTrans = lm_sale_filtered['Txn'].sum().round()
            lmApc = (lmTotalSales/lmTotalTrans).round(2)
            LastWeekSameDaySaleFilter = sale[sale['Trans Date'] == LastWeekSameDay]
            LastWeekSameDaySale = LastWeekSameDaySaleFilter[LastWeekSameDaySaleFilter['Brand'] == dropValueBrand]['NetAmount'].sum().round()

            return f"Last month: {humanizer(lmTotalSales)}", f"Last month: {humanizer(lmTotalTrans)}",f"Last month: {humanizer(lmApc)}", f"Last week SD: {humanizer(LastWeekSameDaySale)}"
        
        else:
            lmStartDate = pd.to_datetime(startdate) + relativedelta.relativedelta(months=-1)
            lmEndDate = pd.to_datetime(enddate) + relativedelta.relativedelta(months=-1)
            LastWeekSameDay = pd.to_datetime(enddate) + relativedelta.relativedelta(days=-7)

            lm_sale_filter = sale[(sale['Trans Date'] >= lmStartDate) & (sale['Trans Date'] <= lmEndDate)].copy()
            lm_sale_filtered = lm_sale_filter[lm_sale_filter['City'] == dropValue]

            lmTotalSales = lm_sale_filtered['NetAmount'].sum().round()
            lmTotalTrans = lm_sale_filtered['Txn'].sum().round()
            lmApc = (lmTotalSales/lmTotalTrans).round(2)
            LastWeekSameDaySaleFilter = sale[sale['Trans Date'] == LastWeekSameDay]
            LastWeekSameDaySale = LastWeekSameDaySaleFilter[LastWeekSameDaySaleFilter['City'] == dropValue]['NetAmount'].sum().round()

            return f"Last month: {humanizer(lmTotalSales)}", f"Last month: {humanizer(lmTotalTrans)}",f"Last month: {humanizer(lmApc)}", f"Last week SD: {humanizer(LastWeekSameDaySale)}"
    
    else:
        if dropValueBrand == "Wow! Momo":
            lmStartDate = pd.to_datetime(startdate) + relativedelta.relativedelta(months=-1)
            lmEndDate = pd.to_datetime(enddate) + relativedelta.relativedelta(months=-1)
            LastWeekSameDay = pd.to_datetime(enddate) + relativedelta.relativedelta(days=-7)

            lm_sale_filter = sale[(sale['Trans Date'] >= lmStartDate) & (sale['Trans Date'] <= lmEndDate)].copy()
            lm_sale_filtered = lm_sale_filter[(lm_sale_filter['City'] == dropValue) & (lm_sale_filter['Brand'] == dropValueBrand)]

            lmTotalSales = lm_sale_filtered['NetAmount'].sum().round()
            lmTotalTrans = lm_sale_filtered['Txn'].sum().round()
            lmApc = (lmTotalSales/lmTotalTrans).round(2)
            LastWeekSameDaySaleFilter = sale[sale['Trans Date'] == LastWeekSameDay]
            LastWeekSameDaySale = LastWeekSameDaySaleFilter[(LastWeekSameDaySaleFilter['City'] == dropValue) & (LastWeekSameDaySaleFilter['Brand'] == dropValueBrand)]['NetAmount'].sum().round()

            return f"Last month: {humanizer(lmTotalSales)}", f"Last month: {humanizer(lmTotalTrans)}",f"Last month: {humanizer(lmApc)}", f"Last week SD: {humanizer(LastWeekSameDaySale)}"
        elif dropValueBrand == "Wow! China":
            lmStartDate = pd.to_datetime(startdate) + relativedelta.relativedelta(months=-1)
            lmEndDate = pd.to_datetime(enddate) + relativedelta.relativedelta(months=-1)
            LastWeekSameDay = pd.to_datetime(enddate) + relativedelta.relativedelta(days=-7)

            lm_sale_filter = sale[(sale['Trans Date'] >= lmStartDate) & (sale['Trans Date'] <= lmEndDate)].copy()
            lm_sale_filtered = lm_sale_filter[(lm_sale_filter['City'] == dropValue) & (lm_sale_filter['Brand'] == dropValueBrand)]

            lmTotalSales = lm_sale_filtered['NetAmount'].sum().round()
            lmTotalTrans = lm_sale_filtered['Txn'].sum().round()
            lmApc = (lmTotalSales/lmTotalTrans).round(2)
            LastWeekSameDaySaleFilter = sale[sale['Trans Date'] == LastWeekSameDay]
            LastWeekSameDaySale = LastWeekSameDaySaleFilter[(LastWeekSameDaySaleFilter['City'] == dropValue) & (LastWeekSameDaySaleFilter['Brand'] == dropValueBrand)]['NetAmount'].sum().round()

            return f"Last month: {humanizer(lmTotalSales)}", f"Last month: {humanizer(lmTotalTrans)}",f"Last month: {humanizer(lmApc)}", f"Last week SD: {humanizer(LastWeekSameDaySale)}"
        elif dropValueBrand == "Combo":
            lmStartDate = pd.to_datetime(startdate) + relativedelta.relativedelta(months=-1)
            lmEndDate = pd.to_datetime(enddate) + relativedelta.relativedelta(months=-1)
            LastWeekSameDay = pd.to_datetime(enddate) + relativedelta.relativedelta(days=-7)

            lm_sale_filter = sale[(sale['Trans Date'] >= lmStartDate) & (sale['Trans Date'] <= lmEndDate)].copy()
            lm_sale_filtered = lm_sale_filter[(lm_sale_filter['City'] == dropValue) & (lm_sale_filter['Brand'] == dropValueBrand)]

            lmTotalSales = lm_sale_filtered['NetAmount'].sum().round()
            lmTotalTrans = lm_sale_filtered['Txn'].sum().round()
            lmApc = (lmTotalSales/lmTotalTrans).round(2)
            LastWeekSameDaySaleFilter = sale[sale['Trans Date'] == LastWeekSameDay]
            LastWeekSameDaySale = LastWeekSameDaySaleFilter[(LastWeekSameDaySaleFilter['City'] == dropValue) & (LastWeekSameDaySaleFilter['Brand'] == dropValueBrand)]['NetAmount'].sum().round()

            return f"Last month: {humanizer(lmTotalSales)}", f"Last month: {humanizer(lmTotalTrans)}",f"Last month: {humanizer(lmApc)}", f"Last week SD: {humanizer(LastWeekSameDaySale)}"
        else:
            lmStartDate = pd.to_datetime(startdate) + relativedelta.relativedelta(months=-1)
            lmEndDate = pd.to_datetime(enddate) + relativedelta.relativedelta(months=-1)
            LastWeekSameDay = pd.to_datetime(enddate) + relativedelta.relativedelta(days=-7)

            lm_sale_filter = sale[(sale['Trans Date'] >= lmStartDate) & (sale['Trans Date'] <= lmEndDate)].copy()
            lm_sale_filtered = lm_sale_filter[(lm_sale_filter['City'] == dropValue)]

            lmTotalSales = lm_sale_filtered['NetAmount'].sum().round()
            lmTotalTrans = lm_sale_filtered['Txn'].sum().round()
            lmApc = (lmTotalSales/lmTotalTrans).round(2)
            LastWeekSameDaySaleFilter = sale[sale['Trans Date'] == LastWeekSameDay]
            LastWeekSameDaySale = LastWeekSameDaySaleFilter[(LastWeekSameDaySaleFilter['City'] == dropValue)]['NetAmount'].sum().round()

            return f"Last month: {humanizer(lmTotalSales)}", f"Last month: {humanizer(lmTotalTrans)}",f"Last month: {humanizer(lmApc)}", f"Last week SD: {humanizer(LastWeekSameDaySale)}"
        


# Starting callbacks for total sales graph...

# Graph no 1 - Total Sales

@app.callback(Output('total-sale-gph','figure'),
              [Input('submit-btn','n_clicks')],
              [State('datePicker','start_date'),
                State('datePicker','end_date'),
                State('dropDBrand','value')])
def sale_filtering(n_clicks,startdate,enddate,dropBrandValue):
    if dropBrandValue == "Wow! Momo":
        sale_filtered = sale[(sale['Trans Date'] >= pd.to_datetime(startdate)) & (sale['Trans Date'] <= pd.to_datetime(enddate))].copy()
        sale_filtered = sale_filtered[sale_filtered['Brand'] == dropBrandValue]
        df_filtered = sale_filtered.groupby(['City'],as_index=False).agg({'NetAmount':'sum'}).round()
        fig = px.pie(df_filtered , names="City", values="NetAmount", title="Net Sales",hole=0.3 )
        
        return fig
    elif dropBrandValue == "Wow! China":
        sale_filtered = sale[(sale['Trans Date'] >= pd.to_datetime(startdate)) & (sale['Trans Date'] <= pd.to_datetime(enddate))].copy()
        sale_filtered = sale_filtered[sale_filtered['Brand'] == dropBrandValue]
        df_filtered = sale_filtered.groupby(['City'],as_index=False).agg({'NetAmount':'sum'}).round()
        fig = px.pie(df_filtered , names="City", values="NetAmount", title="Net Sales",hole=0.3 )
        
        return fig
    elif dropBrandValue == "Combo":
        sale_filtered = sale[(sale['Trans Date'] >= pd.to_datetime(startdate)) & (sale['Trans Date'] <= pd.to_datetime(enddate))].copy()
        sale_filtered = sale_filtered[sale_filtered['Brand'] == dropBrandValue]
        df_filtered = sale_filtered.groupby(['City'],as_index=False).agg({'NetAmount':'sum'}).round()
        fig = px.pie(df_filtered , names="City", values="NetAmount", title="Net Sales",hole=0.3 )
        
        return fig
    else:
        sale_filtered = sale[(sale['Trans Date'] >= pd.to_datetime(startdate)) & (sale['Trans Date'] <= pd.to_datetime(enddate))].copy()
        df_filtered = sale_filtered.groupby(['City'],as_index=False).agg({'NetAmount':'sum'}).round()
        fig = px.pie(df_filtered , names="City", values="NetAmount", title="Net Sales",hole=0.3 )
        
        return fig

# Graph no 2 - Total Transaction

@app.callback(Output('total-txn-gph','figure'),
              [Input('submit-btn','n_clicks')],
              [State('datePicker','start_date'),
                State('datePicker','end_date'),
                State('dropDBrand','value')])
def sale_filtering(n_clicks,startdate,enddate,dropBrandValue):
    if dropBrandValue == "Wow! Momo":
        sale_filtered = sale[(sale['Trans Date'] >= pd.to_datetime(startdate)) & (sale['Trans Date'] <= pd.to_datetime(enddate))].copy()
        sale_filtered = sale_filtered[sale_filtered['Brand'] == dropBrandValue]
        df_filtered = sale_filtered.groupby(['City'],as_index=False).agg({'Txn':'sum'}).round()
        fig = px.pie(df_filtered , names="City", values="Txn", title="Total Transaction",hole=0.3)
        
        return fig
    elif dropBrandValue == "Wow! China":
        sale_filtered = sale[(sale['Trans Date'] >= pd.to_datetime(startdate)) & (sale['Trans Date'] <= pd.to_datetime(enddate))].copy()
        sale_filtered = sale_filtered[sale_filtered['Brand'] == dropBrandValue]
        df_filtered = sale_filtered.groupby(['City'],as_index=False).agg({'Txn':'sum'}).round()
        fig = px.pie(df_filtered , names="City", values="Txn", title="Total Transaction",hole=0.3)
        
        return fig
    elif dropBrandValue == "Combo":
        sale_filtered = sale[(sale['Trans Date'] >= pd.to_datetime(startdate)) & (sale['Trans Date'] <= pd.to_datetime(enddate))].copy()
        sale_filtered = sale_filtered[sale_filtered['Brand'] == dropBrandValue]
        df_filtered = sale_filtered.groupby(['City'],as_index=False).agg({'Txn':'sum'}).round()
        fig = px.pie(df_filtered , names="City", values="Txn", title="Total Transaction",hole=0.3)
        
        return fig
    else:
        sale_filtered = sale[(sale['Trans Date'] >= pd.to_datetime(startdate)) & (sale['Trans Date'] <= pd.to_datetime(enddate))].copy()
        df_filtered = sale_filtered.groupby(['City'],as_index=False).agg({'Txn':'sum'}).round()
        fig = px.pie(df_filtered , names="City", values="Txn", title="Total Transaction",hole=0.3)
        
        return fig

# Graph no 3 - Overall APC

@app.callback(Output('total-apc-gph','figure'),
              [Input('submit-btn','n_clicks')],
              [State('datePicker','start_date'),
                State('datePicker','end_date'),
                State('dropDBrand','value')])
def sale_filtering(n_clicks,startdate,enddate,dropBrandValue):
    if dropBrandValue == "Wow! Momo":
        sale_filtered = sale[(sale['Trans Date'] >= pd.to_datetime(startdate)) & (sale['Trans Date'] <= pd.to_datetime(enddate))].copy()
        sale_filtered = sale_filtered[sale_filtered['Brand'] == dropBrandValue]
        df_filtered = sale_filtered.groupby(['City'],as_index=False).agg({'NetAmount':'sum','Txn':'sum'})
        df_filtered['APC'] = round(df_filtered['NetAmount']/df_filtered['Txn'],2)
        fig = px.bar(df_filtered,x='City',y='APC',title="Overall APC",text="APC",color="APC")
        fig.update_traces(textposition='outside')
        return fig
    elif dropBrandValue == "Wow! China":
        sale_filtered = sale[(sale['Trans Date'] >= pd.to_datetime(startdate)) & (sale['Trans Date'] <= pd.to_datetime(enddate))].copy()
        sale_filtered = sale_filtered[sale_filtered['Brand'] == dropBrandValue]
        df_filtered = sale_filtered.groupby(['City'],as_index=False).agg({'NetAmount':'sum','Txn':'sum'})
        df_filtered['APC'] = round(df_filtered['NetAmount']/df_filtered['Txn'],2)
        fig = px.bar(df_filtered,x='City',y='APC',title="Overall APC",text="APC",color="APC")
        fig.update_traces(textposition='outside')
        return fig
    elif dropBrandValue == "Combo":
        sale_filtered = sale[(sale['Trans Date'] >= pd.to_datetime(startdate)) & (sale['Trans Date'] <= pd.to_datetime(enddate))].copy()
        sale_filtered = sale_filtered[sale_filtered['Brand'] == dropBrandValue]
        df_filtered = sale_filtered.groupby(['City'],as_index=False).agg({'NetAmount':'sum','Txn':'sum'})
        df_filtered['APC'] = round(df_filtered['NetAmount']/df_filtered['Txn'],2)
        fig = px.bar(df_filtered,x='City',y='APC',title="Overall APC",text="APC",color="APC")
        fig.update_traces(textposition='outside')
        return fig
    else:
        sale_filtered = sale[(sale['Trans Date'] >= pd.to_datetime(startdate)) & (sale['Trans Date'] <= pd.to_datetime(enddate))].copy()
        df_filtered = sale_filtered.groupby(['City'],as_index=False).agg({'NetAmount':'sum','Txn':'sum'})
        df_filtered['APC'] = round(df_filtered['NetAmount']/df_filtered['Txn'],2)
        fig = px.bar(df_filtered,x='City',y='APC',title="Overall APC",text="APC",color="APC")
        fig.update_traces(textposition='outside')
        return fig

# Graph no 4 - Sales mode wise

@app.callback(Output('total-mode-sale-gph','figure'),
              [Input('submit-btn','n_clicks')],
              [State('datePicker','start_date'),
                State('datePicker','end_date'),
                State('dropDBrand','value')])
def sale_filtering(n_clicks,startdate,enddate,dropBrandValue):
    if dropBrandValue == "Wow! Momo":
        sale_filtered = sale[(sale['Trans Date'] >= pd.to_datetime(startdate)) & (sale['Trans Date'] <= pd.to_datetime(enddate))].copy()
        sale_filtered = sale_filtered[sale_filtered['Brand'] == dropBrandValue]
        df_filtered = sale_filtered.groupby(['City'],as_index=False).agg({'Dine In Sale':'sum','Delivery Sale':'sum','3rd Party Sale':'sum','Take Away Sale':'sum'}).round()
        fig = px.bar(df_filtered,x='City',y=['Dine In Sale','Delivery Sale','3rd Party Sale','Take Away Sale'],title="Mode Wise Sales")

        return fig
    elif dropBrandValue == "Wow! China":
        sale_filtered = sale[(sale['Trans Date'] >= pd.to_datetime(startdate)) & (sale['Trans Date'] <= pd.to_datetime(enddate))].copy()
        sale_filtered = sale_filtered[sale_filtered['Brand'] == dropBrandValue]
        df_filtered = sale_filtered.groupby(['City'],as_index=False).agg({'Dine In Sale':'sum','Delivery Sale':'sum','3rd Party Sale':'sum','Take Away Sale':'sum'}).round()
        fig = px.bar(df_filtered,x='City',y=['Dine In Sale','Delivery Sale','3rd Party Sale','Take Away Sale'],title="Mode Wise Sales")

        return fig
    elif dropBrandValue == "Combo":
        sale_filtered = sale[(sale['Trans Date'] >= pd.to_datetime(startdate)) & (sale['Trans Date'] <= pd.to_datetime(enddate))].copy()
        sale_filtered = sale_filtered[sale_filtered['Brand'] == dropBrandValue]
        df_filtered = sale_filtered.groupby(['City'],as_index=False).agg({'Dine In Sale':'sum','Delivery Sale':'sum','3rd Party Sale':'sum','Take Away Sale':'sum'}).round()
        fig = px.bar(df_filtered,x='City',y=['Dine In Sale','Delivery Sale','3rd Party Sale','Take Away Sale'],title="Mode Wise Sales")

        return fig
    else:
        sale_filtered = sale[(sale['Trans Date'] >= pd.to_datetime(startdate)) & (sale['Trans Date'] <= pd.to_datetime(enddate))].copy()
        df_filtered = sale_filtered.groupby(['City'],as_index=False).agg({'Dine In Sale':'sum','Delivery Sale':'sum','3rd Party Sale':'sum','Take Away Sale':'sum'}).round()
        fig = px.bar(df_filtered,x='City',y=['Dine In Sale','Delivery Sale','3rd Party Sale','Take Away Sale'],title="Mode Wise Sales")

        return fig

# Graph no 5 - Transaction mode wise

@app.callback(Output('total-mode-txn-gph','figure'),
              [Input('submit-btn','n_clicks')],
              [State('datePicker','start_date'),
                State('datePicker','end_date'),
                State('dropDBrand','value')])
def sale_filtering(n_clicks,startdate,enddate,dropBrandValue):
    if dropBrandValue == "Wow! Momo":
        sale_filtered = sale[(sale['Trans Date'] >= pd.to_datetime(startdate)) & (sale['Trans Date'] <= pd.to_datetime(enddate))].copy()
        sale_filtered = sale_filtered[sale_filtered['Brand'] == dropBrandValue]
        df_filtered = sale_filtered.groupby(['City'],as_index=False).agg({'Dine In Trans':'sum','Delivery Trans':'sum','3rd Party Trans':'sum','Take Away Trans':'sum'}).round()
        fig = px.bar(df_filtered,x='City',y=['Dine In Trans','Delivery Trans','3rd Party Trans','Take Away Trans'],title="Mode Wise Transaction")

        return fig
    elif dropBrandValue == "Wow! China":
        sale_filtered = sale[(sale['Trans Date'] >= pd.to_datetime(startdate)) & (sale['Trans Date'] <= pd.to_datetime(enddate))].copy()
        sale_filtered = sale_filtered[sale_filtered['Brand'] == dropBrandValue]
        df_filtered = sale_filtered.groupby(['City'],as_index=False).agg({'Dine In Trans':'sum','Delivery Trans':'sum','3rd Party Trans':'sum','Take Away Trans':'sum'}).round()
        fig = px.bar(df_filtered,x='City',y=['Dine In Trans','Delivery Trans','3rd Party Trans','Take Away Trans'],title="Mode Wise Transaction")

        return fig
    elif dropBrandValue == "Combo":
        sale_filtered = sale[(sale['Trans Date'] >= pd.to_datetime(startdate)) & (sale['Trans Date'] <= pd.to_datetime(enddate))].copy()
        sale_filtered = sale_filtered[sale_filtered['Brand'] == dropBrandValue]
        df_filtered = sale_filtered.groupby(['City'],as_index=False).agg({'Dine In Trans':'sum','Delivery Trans':'sum','3rd Party Trans':'sum','Take Away Trans':'sum'}).round()
        fig = px.bar(df_filtered,x='City',y=['Dine In Trans','Delivery Trans','3rd Party Trans','Take Away Trans'],title="Mode Wise Transaction")

        return fig
    else:
        sale_filtered = sale[(sale['Trans Date'] >= pd.to_datetime(startdate)) & (sale['Trans Date'] <= pd.to_datetime(enddate))].copy()
        df_filtered = sale_filtered.groupby(['City'],as_index=False).agg({'Dine In Trans':'sum','Delivery Trans':'sum','3rd Party Trans':'sum','Take Away Trans':'sum'}).round()
        fig = px.bar(df_filtered,x='City',y=['Dine In Trans','Delivery Trans','3rd Party Trans','Take Away Trans'],title="Mode Wise Transaction")

        return fig

# Graph no 6 - APC mode wise

@app.callback(Output('total-mode-apc-gph','figure'),
              [Input('submit-btn','n_clicks')],
              [State('datePicker','start_date'),
                State('datePicker','end_date'),
                State('dropDBrand','value')])
def sale_filtering(n_clicks,startdate,enddate,dropBrandValue):
    if dropBrandValue == "Wow! Momo":    
        sale_filtered = sale[(sale['Trans Date'] >= pd.to_datetime(startdate)) & (sale['Trans Date'] <= pd.to_datetime(enddate))].copy()
        sale_filtered = sale_filtered[sale_filtered['Brand'] == dropBrandValue]
        df_filtered = sale_filtered.groupby(['City'],as_index=False).agg(
                                                                        {'Dine In Sale':'sum',
                                                                        'Delivery Sale':'sum',
                                                                        '3rd Party Sale':'sum',
                                                                        'Take Away Sale':'sum',
                                                                        'Dine In Trans':'sum',
                                                                        'Delivery Trans':'sum',
                                                                        '3rd Party Trans':'sum',
                                                                        'Take Away Trans':'sum',
                                                                        }).round()
        df_filtered['Dine In APC'] = round(df_filtered['Dine In Sale']/df_filtered['Dine In Trans'],2)
        df_filtered['Delivery APC'] = round(df_filtered['Delivery Sale']/df_filtered['Delivery Trans'],2)
        df_filtered['3rd Party APC'] = round(df_filtered['3rd Party Sale']/df_filtered['3rd Party Trans'],2)
        df_filtered['Take Away APC'] = round(df_filtered['Take Away Sale']/df_filtered['Take Away Trans'],2)
        fig = px.bar(df_filtered,x='City',
                                    y=['Dine In APC',
                                            'Delivery APC',
                                            '3rd Party APC',
                                            'Take Away APC'],
                                            title="Mode Wise APC")

        return fig
    elif dropBrandValue == "Wow! China":    
        sale_filtered = sale[(sale['Trans Date'] >= pd.to_datetime(startdate)) & (sale['Trans Date'] <= pd.to_datetime(enddate))].copy()
        sale_filtered = sale_filtered[sale_filtered['Brand'] == dropBrandValue]
        df_filtered = sale_filtered.groupby(['City'],as_index=False).agg(
                                                                        {'Dine In Sale':'sum',
                                                                        'Delivery Sale':'sum',
                                                                        '3rd Party Sale':'sum',
                                                                        'Take Away Sale':'sum',
                                                                        'Dine In Trans':'sum',
                                                                        'Delivery Trans':'sum',
                                                                        '3rd Party Trans':'sum',
                                                                        'Take Away Trans':'sum',
                                                                        }).round()
        df_filtered['Dine In APC'] = round(df_filtered['Dine In Sale']/df_filtered['Dine In Trans'],2)
        df_filtered['Delivery APC'] = round(df_filtered['Delivery Sale']/df_filtered['Delivery Trans'],2)
        df_filtered['3rd Party APC'] = round(df_filtered['3rd Party Sale']/df_filtered['3rd Party Trans'],2)
        df_filtered['Take Away APC'] = round(df_filtered['Take Away Sale']/df_filtered['Take Away Trans'],2)
        fig = px.bar(df_filtered,x='City',
                                    y=['Dine In APC',
                                            'Delivery APC',
                                            '3rd Party APC',
                                            'Take Away APC'],
                                            title="Mode Wise APC")

        return fig
    elif dropBrandValue == "Combo":    
        sale_filtered = sale[(sale['Trans Date'] >= pd.to_datetime(startdate)) & (sale['Trans Date'] <= pd.to_datetime(enddate))].copy()
        sale_filtered = sale_filtered[sale_filtered['Brand'] == dropBrandValue]
        df_filtered = sale_filtered.groupby(['City'],as_index=False).agg(
                                                                        {'Dine In Sale':'sum',
                                                                        'Delivery Sale':'sum',
                                                                        '3rd Party Sale':'sum',
                                                                        'Take Away Sale':'sum',
                                                                        'Dine In Trans':'sum',
                                                                        'Delivery Trans':'sum',
                                                                        '3rd Party Trans':'sum',
                                                                        'Take Away Trans':'sum',
                                                                        }).round()
        df_filtered['Dine In APC'] = round(df_filtered['Dine In Sale']/df_filtered['Dine In Trans'],2)
        df_filtered['Delivery APC'] = round(df_filtered['Delivery Sale']/df_filtered['Delivery Trans'],2)
        df_filtered['3rd Party APC'] = round(df_filtered['3rd Party Sale']/df_filtered['3rd Party Trans'],2)
        df_filtered['Take Away APC'] = round(df_filtered['Take Away Sale']/df_filtered['Take Away Trans'],2)
        fig = px.bar(df_filtered,x='City',
                                    y=['Dine In APC',
                                            'Delivery APC',
                                            '3rd Party APC',
                                            'Take Away APC'],
                                            title="Mode Wise APC")

        return fig
    else:
        sale_filtered = sale[(sale['Trans Date'] >= pd.to_datetime(startdate)) & (sale['Trans Date'] <= pd.to_datetime(enddate))].copy()
        df_filtered = sale_filtered.groupby(['City'],as_index=False).agg(
                                                                        {'Dine In Sale':'sum',
                                                                        'Delivery Sale':'sum',
                                                                        '3rd Party Sale':'sum',
                                                                        'Take Away Sale':'sum',
                                                                        'Dine In Trans':'sum',
                                                                        'Delivery Trans':'sum',
                                                                        '3rd Party Trans':'sum',
                                                                        'Take Away Trans':'sum',
                                                                        }).round()
        df_filtered['Dine In APC'] = round(df_filtered['Dine In Sale']/df_filtered['Dine In Trans'],2)
        df_filtered['Delivery APC'] = round(df_filtered['Delivery Sale']/df_filtered['Delivery Trans'],2)
        df_filtered['3rd Party APC'] = round(df_filtered['3rd Party Sale']/df_filtered['3rd Party Trans'],2)
        df_filtered['Take Away APC'] = round(df_filtered['Take Away Sale']/df_filtered['Take Away Trans'],2)
        fig = px.bar(df_filtered,x='City',
                                    y=['Dine In APC',
                                        'Delivery APC',
                                            '3rd Party APC',
                                            'Take Away APC'],
                                            title="Mode Wise APC")

        return fig