import numpy as np
from scipy import optimize


def get_length(theta,b):
  """Get the spiral length (L) given theta and b"""
  aux = np.sqrt(1.0+theta**2)
  return 0.5*b*(theta*aux + np.log(theta+aux))

def get_b(theta,L):
  """Get the parameter b given theta and L"""
  aux = np.sqrt(1.0+theta**2)
  return 2.0*L/(theta*aux + np.log(theta+aux))

def eq_theta(theta,b,L):
  """equation to minimize given theta, b and L (length)"""
  aux = np.sqrt(1.0+theta**2)
  return L - 0.5*b*(theta*aux + np.log(theta+aux))

def get_theta(guess_theta,b,L):
  """Get the theta given b and L (length)"""
  sol = optimize.root(eq_theta,[guess_theta],args=(b,L))
  return sol



def spiral(L0):
    numpis = 8.0  # numero de voltas (multiplo de pi)
    numpts = 100  # numero de pontos para a curva gerada
    a = 0.0  # o código ainda não contempla a > 0
    b = get_b(numpis * np.pi, L0)
    interlayer = round(2.0 * np.pi * b, 1)
    theta = 0.0  # valor do angulo, onde começa o scroll

    dtheta = (numpis * np.pi) / numpts  # !(4.0*np.pi)/numpts

    # !write(*,*) 'r inicial  (padrao r = a)'
    # !read(*,*) r
    # Initial theta
    # if b == 0.0:
    #  theta = 0.0
    # else:
    #  theta = 0.0 #2*np.pi #!(r-a)/b
    list_path = []
    for _ in range(numpts):
        r = a + b * theta
        x = r * np.cos(theta)
        y = r * np.sin(theta)
        # f.write(x,y)
        ax = round(x, 4)
        ay = round(y, 4)
        text = " {" + str(ax) + " 0.0 " + str(ay) + "} "
        theta = theta + dtheta
        list_path.append(text)

    path = ''.join(list_path)
    return path



