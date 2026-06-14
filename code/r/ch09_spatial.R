# Chapter 9 - Spatial analysis and crime mapping
# Read points, estimate a density surface, and test clustering with Moran's I.
# Needs: install.packages(c("sf", "spatstat", "spdep"))

# --- book code (Chapter 9) -------------------------------------------------
# R: install the spatial packages once, then load them each session
# install.packages(c("sf", "spatstat", "spdep"))
library(sf)        # store and handle points with coordinates
library(spatstat)  # kernel density and point-pattern tools
library(spdep)     # neighbours, weights, and Moran's I

# R: read a CSV of incidents and plot the raw points
crime <- read.csv(file.path("data", "synthetic", "burglary.csv"))
pts <- st_as_sf(crime,
                coords = c("easting", "northing"),
                crs = 27700)                 # British National Grid
plot(st_geometry(pts), pch = 20, cex = 0.5)  # quick look at the dots

# R: kernel density, then Moran's I on grid counts with 999 permutations
library(spatstat.geom)
win  <- as.owin(st_bbox(pts))                 # the study area
ppp_obj <- as.ppp(st_coordinates(pts), W = win)
dens <- density(ppp_obj, sigma = 250)         # 250 m bandwidth; justify it
plot(dens, main = "Burglary density")

grid <- st_make_grid(pts, cellsize = 500)     # 500 m cells
counts <- lengths(st_intersects(grid, pts))   # crimes per cell
nb <- poly2nb(as(grid, "Spatial"))            # who neighbours whom
w  <- nb2listw(nb, zero.policy = TRUE)        # turn neighbours into weights
moran.mc(counts, w, nsim = 999, zero.policy = TRUE)  # test by permutation
