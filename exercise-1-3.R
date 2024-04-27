pacman::p_load(pacman, MDPtoolbox)

r <- array(0, c(2, 2, 2))
r[,,1] <- matrix(c(100,  10, 100, 200), 2, 2, byrow=T)
r[,,2] <- matrix(c( 50,  50,  60,  80), 2, 2, byrow=T)

p <- array(0, c(2, 2, 2))
p[,,1] <- matrix(c(0.6, 0.4, 0.5, 0.5), 2, 2, byrow=T)
p[,,2] <- matrix(c(0.2, 0.8, 0.5, 0.5), 2, 2, byrow=T)

mdp_finite_horizon(p, r, 0.8, 4)
