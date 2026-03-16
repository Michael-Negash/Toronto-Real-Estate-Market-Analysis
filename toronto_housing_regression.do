
// get a best fit for the Bond vs Toronto Stock Exchange  scatter plot
predict BestFitTSX, xb
//Bond vs Toronto Stock Exchange  scatter plot
twoway (scatter BONDS TSX, sort) (line BestFitTSX TSX, sort), title("Bond vs Toronto Stock Exchange", size(small)) xtitle("Toronto Stock Exchange") ytitle("Bonds", size(small)) 
// regression analysis
regress BONDS TSX



// get a best fit for the Toronto Population vs Average Sale Price
twoway  (scatter AVGPT POP, sort)   , title("Toronto Population vs Average Sale Price", size(small)) xtitle("Toronto Population(000)") ytitle("Average Sale Price(000)", size(small)) 
// regression analysis
regress AVGPT POP

// get a best fit for the Toronto Population vs Price Index
twoway  (scatter THPI POP, sort)   , title("Toronto Population vs Price Index", size(small)) xtitle("Toronto Population(000)") ytitle("Toronto House Price Index", size(small)) 

// get a best fit for the Toronto Population vs Price Index Two Storey Houses
twoway  (scatter THPIH  POP, sort)   , title("Toronto Population vs Price Index Two Storey Houses", size(small)) xtitle("Toronto Population(000)") ytitle("Toronto House Price Index Two Storey Houses", size(small)) 

// get a best fit for the Toronto Population vs Price Index Apartments/Condos
twoway  (scatter THPIA POP, sort)   , title("Toronto Population vs Price Index Apartments/Condos", size(small)) xtitle("Toronto Population(000)") ytitle("Toronto House Price Index Apartments/Condos)", size(small)) 

// regression analysis
 regress POP THPI THPIH THPIA
 
 
//correlation matrix provides insight into the relationships between variables
correlate THPI THPIH THPIA POP

// regression analysis
regress AVGPT LFC  PTM  UNEMP EI

// correlation between part-time employment, unemployment, and employment insurance
 correlate PTM UNEMP EI
 
 
// regression analysis
 regress CPIT RETAIL CNEWHL  RENT OWN
