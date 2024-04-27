pacman::p_load(pacman, MDPtoolbox)

r <- array(0, c(3, 3, 2))
r[,,1] <- matrix(nrow=3, ncol=3, byrow=T,
                 c(100,  50, 150,
                    50, 100, 200,
                   100, 200,  50))
r[,,2] <- matrix(nrow=3, ncol=3, byrow=T,
                 c( 50,  50, 100,
                   100, 150,  50,
                   100, 150,  50))

p <- array(0, c(3, 3, 2))
p[,,1] <- matrix(nrow=3, ncol=3, byrow=T,
                 c(0.2, 0.5, 0.3,
                   0.3, 0.6, 0.1,
                   0.2, 0.2, 0.6))
p[,,2] <- matrix(nrow=3, ncol=3, byrow=T,
                 c(0.5, 0.2, 0.3,
                   0.3, 0.2, 0.5,
                   0.7, 0.1, 0.2))

mdp_policy_iteration(p, r, 0.9)