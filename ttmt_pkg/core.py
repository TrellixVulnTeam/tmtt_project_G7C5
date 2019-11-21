"""
-----------------------------------------------------------------------------
=============================================================================
----------- TMTT - Text Mining de Textes Techniques - 09/2019- --------------
---------------------------------JRubio--------------------------------------
=============================================================================

----------------------------------------
------------ FICHIER CORE --------------
----------------------------------------
"""

import config as cfg
import analyse_text as at
# from progress.bar import IncrementalBar

texte = 'En se réveillant un matin après des rêves agités, Gregor Samsa se retrouva, dans son lit, métamorphosé en un monstrueux insecte. Il était sur le dos, un dos aussi dur qu’une carapace, et, en relevant un peu la tête, il vit, bombé, brun, cloisonné par des arceaux plus rigides, son abdomen sur le haut duquel la couverture, prête à glisser tout à fait, ne tenait plus qu’à peine. Ses nombreuses pattes, lamentablement grêles par comparaison avec la corpulence qu’il avait par ailleurs, grouillaient désespérément sous ses yeux.« Qu’est-ce qui m’est arrivé ? » pensa-t-il. Ce n’était pas un rêve. Sa chambre, une vraie chambre humaine, juste un peu trop petite, était là tranquille entre les quatre murs qu’il connaissait bien. Au-dessus de la table où était déballée une collection d’échantillons de tissus - Samsa était représentant de commerce - on voyait accrochée l’image qu’il avait récemment découpée dans un magazine et mise dans un joli cadre doré. Elle représentait une dame munie d’une toque et d’un boa tous les deux en fourrure et qui, assise bien droite, tendait vers le spectateur un lourd manchon de fourrure où tout son avant-bras avait disparu. Le regard de Gregor se tourna ensuite vers'

print('Hello World \n')
print('----> Vérification des accès aux différents dossiers \n')

cfg.test_tous_chemins(cfg.chemins)  # Test de la configuration

print('----> Début de l\'analyse textuelle \n')

# bar = IncrementalBar('Processing', max=20)
# for i in range(20):
#    bar.next()

print('\n')
texte = at.supp_majuscule(texte)

texte = at.supp_nombre(texte)

texte = at.supp_ponctuation(texte)

texte = at.supp_espace(texte)

texte = at.token(texte)

# bar.finish()
