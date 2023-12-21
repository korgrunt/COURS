

1   Quelles sont les grandes étapes à suivre pour comprendre le fonctionnement (ingénerie à reculons) d'un système éléctronique ?

    Pour comprendre le fonctionnement d'un system electronique, il faut connaitre ses composants, comment il sont connecté entre eux, leurs role respectif, et créer un schema electronique par exemple.
    Par exemple, sur un circuit imprimé, il y a plusieur couche dans lesquels passe l'alimentation, les donné echangé, les IO.
    On peut aussi se brancher sur les IO ou les connecteur de test pour comprendre le foncitonnement hardware 

2   Quelles menaces doivent être prises en compte si l'on considère que l'attaquant dispose d'un accès physique à un système embarqué cible ?

    Les attaque par DMA, donc, l'acces au connection, a la lecture de la mémoire, a l'analyse logique des signaux qui passe dans les fils. L'attaquant sera en capacité d'ouvrire le boitié, et en fonction de son objectif (reproduction de la techno, lecture des donné, implantation de puces espion)? Il pourra aussi détourné des fonctionnalité a sont profit, par exemple, utiliséer les registre de stockage de config pour faire de l'evasion de donnée via un ecran, ou autre periphérique.


3   Pourquoi est il important de sécuriser la chaine de démarrage ?

    Car si on ne securise pas une chaine de boot, l'attaquant sera en capacité de modifier l'execution de l'os, et y inserer ses propre implémentation comportement.

4   Sur quel(s) élément(s) repose une chaîne de démarrage sécurisée ?

    Le secure boot, le bios, la memoire flash de boot, eventuellement, des clée de chiffrement/signature.

5   Qu'est-ce qu'un analyseur logique ? Pourquoi est-ce un équipement utile pour un attaquant ?

    Un analyser logique est un outils electronique permettant de sniffé les signaux eletrique ( ou electronmagnetique) afin de répliqué les donné qui transite sur les connection eletronique et ainsi espionner les echange de donné entre des composants.

6   Lorsque l'on considère un protocole de communication au niveau couche physique, quel est le rôle du signal d'horloge ?

    Le roe du signal d'horloge a pour but de syncroniser les composants entre eux afin qu'il echange des bit via des signaux eletrique en respectant le protocole utilisé dans le circuit imprimé (I2C par exemple)

7   A quoi sert le protocole JTAG ? Pourquoi est il important d'en protéger l'accès ?

    Le protocol JTAG est un protocol qui permet de tester les composant qui sont fortement intégré. des port jtag sont dispo sur les carte electronique, souvent se sont des petit regroupement de rond de cuivre sur lequel les testeur se connect pour verifier si les IO d'un composant sont correct ( il envoi un signal sur tel port jtag, et attende un signal spécifique sur un autre, ce qui leur permet de valider le foncitonnement du composant intégré a la carte asser rapidement)
    Il est impératif de s'en protéger car ils peuvetnt être exploiter dans la retro ingienerie d'un circutit imprimé et de ses composant, ce qui permettrai a l'attaquand de trouver des exploit plus rapidement. 
    Dans certain cas, il peuvent être utiliser directement pour faire des attaque par glitch, par snif de signal car il permette une communication direct avec le composant.

8   A quoi sert le protocole I2C?

    Le protocole i2c sert a transmetre de la donné entre les composant d'un circuit imprimé, c'est un bus bedirectionnel en half duplex.

9   Qu'est ce qu'une attaque par glitch ?

    Le principe d'une attaque glitch consiste a fournire des perturbation pendant le foncitonnement d'un composant pour changer sont etat. Cela permet de soit, changer des instruction ,soit, corompre des registre dand de la mémoire pour en alterré leurs foncitonnement.

    on peut aussi amener une  perturbation en ralentisant l'horloge, cela rendra plus simple l'analyse des échanges de donné, mais aussi, peut potentiellement affecté certain composant, et d'autre non. Le processeur par exemple sera amener a executer des instruction différente, ou a des moment ou la memoire est dans un état différent que l'état dans lequel elle aurait été.

10  Quel est le principe d'une Timing Attack (expliquer d'ou vient le problème) ? Comment y remédier ?

    Le timing attaque consiste a l'analyse des signaux transitant dans un system electronique pour en extraire des donné, et ainsi, le temps qui est mis par les composant pour faire tel ou tel action, et ainsi, en extraire des secret. Par exemple, pour la verification d'un mot de passe, on peut analyser le temps que met le system a répondre non a achaque essaies, et ainsi déduire la ou il y a une erreur dans le mot de passe fournit. Il mettra par exemple 1 milliseconde si le premier character est faux, 2 millisecodne si le 2 eme caractere est faux, et ainsi de suite.
    Pour y remedier, on peut mettre un temps par default d'attente, et implémenter cela dans l'algo pour que peut importe la proximité du vrai mot de passe avec le mot de passe essayé par l'ataquant ,le system mettent toujours 1 seconde a répondre.

    On a le même probléme avec la consomation d'energie par exemple, en analysant la consomation d'un composant, on peut déduire les actions qu'il est en train de faire. Pour les carte a puce, les ingénieur ont implémenter des action random qui sont fait même quand la carte a puce ne fait rien pour lisser la consomation et rendre l'analyse de signal inutile.