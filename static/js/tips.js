$('#tips').empty();

var r_text = new Array ();
r_text[0] = "Choose steamed, stewed, braised or stir-fried dishes instead of fried, sweet and sour or deep-fried dishes.";
r_text[1] = "Choose dishes without added fat in the gravy instead of curry dishes and curry gravy.";
r_text[2] = "Choose stir-fried vegetables with soya sauce or oyster sauce instead of chilli-based sauce dishes.";
r_text[3] = "Order chicken and duck dishes without the skin.";
r_text[4] = "Order more vegetable-based dishes. Try substituting meat with tofu instead of ordering only meat dishes.";
r_text[5] = "Ask for less rice - most economy rice stalls give too much.";
r_text[6] = "Choose soup-based noodles or ask for no added oil in dry noodles dishes instead of dry or fried noodles.";
r_text[7] = "Choose noodle dishes without added fat in gravy instead of coconut milk-based dishes";
r_text[8] = "Choose sliced red chilli or pickled green chilli (but go easy on the light soya sauce to prevent excessive salt intake) as a condiment instead of sambal chilli";
r_text[9] = "Choose sliced meat instead of minced meat.";
r_text[10] = "Choose garnishings that are not fried.";
r_text[11] = "General rule: Healthy meals are cooked with less oil/fat; have less sugar; have more fibre.";
r_text[12] = "When ordering chicken rice, ask for steamed white rice and remove the skin from the chicken.";
r_text[13] = "Avoid roti prata (pratha), puri or bhatura, but choose chapati, dosa (thosai) or idli with chickpeas and dahl (lentil) chutney instead. Omit the coconut chutney.";
r_text[14] = "Instead of lontong, mee rebus or mee siam, choose chicken macaroni soup or bee hoon soto.";
r_text[15] = "Choose mineral water or tea/coffee with less sugar and less evaporated milk/condensed milk.";
r_text[16] = "Choose fresh fruit and limit desserts to twice a week (choose those without coconut milk and also ask for less sugar).";
r_text[17] = "'I think nutrition is very important. I try to stay away from heavy cooking because it takes away much of the vitamins in food. I also try to avoid caffeine.' - Singapore's 113-Year-Old Teresa Hsu";
r_text[18] = "'Overall, my eating habits are very simple: I consume a lot of foods like avocado, milk, beans and raw eggs that are high in nutrients like proteins and omega-3.' - Singapore's 113-Year-Old Teresa Hsu";
r_text[19] = "'Health is the greatest gift, contentment the greatest wealth, faithfulness the best relationship.' - Buddha";
r_text[20] = "'He who enjoys good health is rich, though he knows it not.' - Anonymous";
r_text[21] = "'Our health always seems much more valuable after we lose it.' - Anonymous";
var i = Math.floor(22*Math.random());


$('#tips').append(r_text[i]);