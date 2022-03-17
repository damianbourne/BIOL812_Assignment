#BIOL812 assignment part C 
library(dplyr)
library(ggplot2)
library(gridExtra)


dat <- read.csv("dna_output.csv")

prop <- function(X){
  proportion <- X/sum(X)
  return(proportion)
}

dat <- dat %>% mutate(A_prop = prop(A), T_prop = prop(T),
                      G_prop = prop(G), C_prop = prop(C))


F1 <- ggplot(dat, aes(x = A_prop)) +
  geom_histogram()
F2 <- ggplot(dat, aes(x = T_prop)) +
  geom_histogram()
F3 <- ggplot(dat, aes(x = G_prop)) +
  geom_histogram()
F4 <- ggplot(dat, aes(x = C_prop)) +
  geom_histogram()

pdf("PartC_Plot.pdf")
grid.arrange(F1, F2, F3, F4, ncol = 2)
dev.off()

