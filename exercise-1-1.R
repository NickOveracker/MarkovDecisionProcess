pacman::p_load(pacman, MDPtoolbox)

r <- array(0, c(2, 2, 2))
r[,,1] <- matrix(c(100, 150, 200, 50), 2, 2, byrow=T)
r[,,2] <- matrix(c(120, 100, 120, 80), 2, 2, byrow=T)

p <- array(0, c(2, 2, 2))
p[,,1] <- matrix(c(0.8, 0.2, 0.7, 0.3), 2, 2, byrow=T)
p[,,2] <- matrix(c(0.2, 0.8, 0.6, 0.4), 2, 2, byrow=T)

mdp_finite_horizon(p, r, 0.9, 4)