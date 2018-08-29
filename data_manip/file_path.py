mandarin_kugou_root = '/Users/ronggong/Documents_using/MTG_document/dataset/Lyrics-to-Audio_Alignment_training_data/kugou/'

mir1k_root = '/Users/ronggong/Documents_using/MTG_document/dataset/MIR-1K'

hansen_root = '/Users/ronggong/Documents_using/MTG_document/dataset/hansen_dataset'

mauch_root = '/Users/ronggong/Documents_using/MTG_document/dataset/Lyrics2Audio_Dataset'

gracenote_root = '/Users/ronggong/Documents_using/MTG_document/dataset/lyrics_dataset'

jingju_part1_root = '/Users/ronggong/Documents_using/MTG_document/Jingju_arias/jingju_a_cappella_singing_dataset'

jingju_part2_root = '/Users/ronggong/Documents_using/MTG_document/Jingju_arias/jingju_a_cappella_singing_dataset_extended_nacta2017'

jingju_part3_root = '/Users/ronggong/Documents_using/MTG_document/Jingju_arias/primary_school_recording'


def get_recording_names_jingju():
    train_dan_ss = [['danAll', 'zhuangyuanmei_tianbofu'],
                    ['danAll', 'zhuangyuanmei_fudingkui'],
                    ['danAll', 'zhuangyuanmei_zinari'],
                    ['danAll', 'xixiangji_biyuntian'],
                    ['danAll', 'xixiangji_zhenmeijiu'],
                    ['danAll', 'zhuangyuanmei_zhenzhushan'],
                    ['danAll', 'xixiangji_manmufeng'],
                    ['danAll', 'wangjiangting_zhijianta'],
                    ['danAll', 'wangjiangting_dushoukong'],
                    ['danAll', 'xixiangji_diyilai'],
                    ['danAll', 'xixiangji_xianzhishuo'],
                    ['danAll', 'shiwenhui_tingxiongyan']]

    dev_dan_ss = [['danAll', 'zhuangyuanmei_daocishi'],
                  ['danAll', 'xixiangji_luanchouduo'],
                  ['danAll', 'yutangchun_yutangchun']]

    train_dan_nacta = [['danAll', 'danbz-Kan_dai_wang-Ba_wang_bie_ji03-qm'],
                       ['danAll', 'daxp-Chun_qiu_ting-Suo_lin_nang01-qm'],
                       ['danAll', 'daxp-Guan_Shi_yin-Tian_nv_san_hua-lon'],
                       ['danAll', 'danbz-Bei_jiu_chan-Chun_gui_men03-qm'],
                       ['danAll', 'daxp-Meng_ting_de-Mu_Gui_ying_gua_shuai06-qm'],
                       ['danAll', 'daspd-Hai_dao_bing-Gui_fei_zui_jiu02-qm'],
                       ['danAll', 'daeh-Yi_sha_shi-Suo_lin_nang-qm'],
                       ['danAll', 'daspd-Hai_dao_bing-Gui_fei_zui_jiu01-lon'],
                       ['danAll', 'danbz-Bei_jiu_chan-Chun_gui_men01-qm'],
                       ['danAll', 'daxp-Meng_ting_de-Mu_Gui_ying_gua_shuai04-qm'],
                       ['danAll', 'daspd-Du_shou_kong-Wang_jiang_ting-upf'],
                       ['danAll', 'daxp-Zhe_cai_shi-Suo_lin_nang01-qm'],
                       ['danAll', 'daxp-Xi_ri_li-Gan_lu_si-qm'],
                       ['danAll', 'danbz-Kan_dai_wang-Ba_wang_bie_ji01-qm'],
                       ['danAll', 'daxp-Meng_ting_de-Mu_Gui_ying_gua_shuai02-qm'],
                       ['danAll', 'daxp-Jiao_Zhang_sheng-Hong_niang04-qm'],
                       ['danAll', 'daxp-Chun_qiu_ting-Suo_lin_nang03-qm'],
                       ['danAll', 'daxp-Meng_ting_de-Mu_Gui_ying_gua_shuai01-upf'],
                       ['danAll', 'daxp-Jiao_Zhang_sheng-Hong_niang01-qm'],
                       ['danAll', 'daeh-Bie_yuan_zhong-Mei_fei-qm'],
                       ['danAll', 'daeh-Yang_Yu_huan-Tai_zhen_wai_zhuan-lon'],
                       ['danAll', 'daxp-Jiao_Zhang_sheng-Hong_niang05-qm'], ]

    dev_dan_nacta = [['danAll', 'dagbz-Feng_xiao_xiao-Yang_men_nv_jiang-lon'],
                     ['danAll', 'danbz-Qing_chen_qi-Shi_yu_zhuo-qm'],
                     ['danAll', 'dafeh-Bi_yun_tian-Xi_xiang_ji01-qm'],
                     ['danAll', 'daeh-You_He_hou-He_hou_ma_dian-qm'],
                     ['danAll', 'dafeh-Mo_lai_you-Liu_yue_xue-qm'], ]

    train_dan_primary = [['20171211SongRuoXuan/daxp-Fei_shi_wo-Hua_tian_cuo-dxjky', 'teacher'],
                         ['20171211SongRuoXuan/daxp-Meng_ting_de-Mu_gui_ying_gua_shuai-dxjky', 'teacher'],
                         ['20171214SongRuoXuan/daeh-Yang_yu_huan-Tai_zhen_wai_zhuan-nanluo', 'teacher'],
                         ['20171214SongRuoXuan/danbz-Kan_dai_wang-Ba_wang_bie_ji-nanluo', 'teacher'],
                         ['20171214SongRuoXuan/daspd-Hai_dao_bing-Gui_fei_zui_jiu-nanluo', 'teacher'],
                         ['20171215SongRuoXuan/daxp-Jiao_zhang_sheng-Xi_shi-qianmen', 'teacher'],
                         ['2017121215SongRuoXuan/daxp-Mu_qin_bu_ke-Feng_huan_chao-yucai_qianmen', 'teacher'],
                         ['20171214SongRuoXuan/daxp-Quan_jun_wang-Ba_wang_bie_ji-nanluo', 'teacher'],

                         ['20171214SongRuoXuan/daeh-Yang_yu_huan-Tai_zhen_wai_zhuan-nanluo', 'student_01'],
                         ['20171214SongRuoXuan/daeh-Yang_yu_huan-Tai_zhen_wai_zhuan-nanluo', 'student_02'],
                         ['20171214SongRuoXuan/daeh-Yang_yu_huan-Tai_zhen_wai_zhuan-nanluo', 'student_02'],
                         ['20171214SongRuoXuan/daeh-Yang_yu_huan-Tai_zhen_wai_zhuan-nanluo', 'student_04'],
                         ['20171214SongRuoXuan/daeh-Yang_yu_huan-Tai_zhen_wai_zhuan-nanluo', 'student_05'],

                         ['20171214SongRuoXuan/danbz-Kan_dai_wang-Ba_wang_bie_ji-nanluo', 'student_01'],
                         ['20171214SongRuoXuan/danbz-Kan_dai_wang-Ba_wang_bie_ji-nanluo', 'student_02'],
                         ['20171214SongRuoXuan/danbz-Kan_dai_wang-Ba_wang_bie_ji-nanluo', 'student_03'],

                         ['20171214SongRuoXuan/daxp-Quan_jun_wang-Ba_wang_bie_ji-nanluo', 'student_01'],
                         ['20171214SongRuoXuan/daxp-Quan_jun_wang-Ba_wang_bie_ji-nanluo', 'student_02'],
                         ['20171214SongRuoXuan/daxp-Quan_jun_wang-Ba_wang_bie_ji-nanluo', 'student_03'],

                         ['20171215SongRuoXuan/daxp-Jiao_zhang_sheng-Xi_shi-qianmen', 'student_01'],
                         ['20171215SongRuoXuan/daxp-Jiao_zhang_sheng-Xi_shi-qianmen', 'student_02'],
                         ['20171215SongRuoXuan/daxp-Jiao_zhang_sheng-Xi_shi-qianmen', 'student_03'],
                         ['20171215SongRuoXuan/daxp-Jiao_zhang_sheng-Xi_shi-qianmen', 'student_04'],
                         ['20171215SongRuoXuan/daxp-Jiao_zhang_sheng-Xi_shi-qianmen', 'student_05'],
                         ['20171215SongRuoXuan/daxp-Jiao_zhang_sheng-Xi_shi-qianmen', 'student_06'],
                         # ['2017121215SongRuoXuan/daxp-Mu_qin_bu_ke-Feng_huan_chao-yucai_qianmen', 'student_01_qianmen'],
                         # ['2017121215SongRuoXuan/daxp-Mu_qin_bu_ke-Feng_huan_chao-yucai_qianmen', 'student_02_qianmen'],
                         # ['2017121215SongRuoXuan/daxp-Mu_qin_bu_ke-Feng_huan_chao-yucai_qianmen', 'student_03_qianmen'],
                         # ['2017121215SongRuoXuan/daxp-Mu_qin_bu_ke-Feng_huan_chao-yucai_qianmen', 'student_04_qianmen'],
                         # ['2017121215SongRuoXuan/daxp-Mu_qin_bu_ke-Feng_huan_chao-yucai_qianmen', 'student_05_qianmen'],
                         # ['2017121215SongRuoXuan/daxp-Mu_qin_bu_ke-Feng_huan_chao-yucai_qianmen', 'student01_yucai'],
                         # ['2017121215SongRuoXuan/daxp-Mu_qin_bu_ke-Feng_huan_chao-yucai_qianmen', 'student02_yucai'],
                         # ['2017121215SongRuoXuan/daxp-Mu_qin_bu_ke-Feng_huan_chao-yucai_qianmen', 'student03_yucai']]
                         ]

    dev_dan_primary = [['20171211SongRuoXuan/daxp_Qing_zao_qi_lai-Mai_shui-dxjky', 'teacher'],
                       ['20171211SongRuoXuan/daxp-Wo_jia_di-Hong_deng_ji-dxjky', 'teacher'],
                       ['20171214SongRuoXuan/daspd-Hai_dao_bing-Gui_fei_zui_jiu-nanluo', 'student_01'],
                       ['20171214SongRuoXuan/daspd-Hai_dao_bing-Gui_fei_zui_jiu-nanluo', 'student_02'], ]

    train_laosheng_nacta = [['laosheng', 'lsfxp-Yang_si_lang-Si_lang_tan_mu-lon'],
                            ['laosheng', 'lsxp-Jiang_shen_er-San_jia_dian01-1-upf'],
                            ['laosheng', 'lsxp-Xi_ri_you-Zhu_lian_zhai-qm'],
                            ['laosheng', 'lsxp-Guo_liao_yi-Wen_zhao_guan01-upf'],
                            ['laosheng', 'lsxp-Shen_gong_wu-Gan_lu_si-qm'],
                            ['laosheng', 'lsxp-Wo_zheng_zai-Kong_cheng_ji01-upf'],
                            ['laosheng', 'lseh-Yi_lun_ming-Wen_zhao_guan-qm'],
                            ['laosheng', 'lseh-Wei_guo_jia-Hong_yang_dong02-qm'],
                            ['laosheng', 'lsxp-Huai_nan_wang-Huai_he_ying01-lon'],
                            ['laosheng', 'lsxp-Guo_liao_yi-Wen_zhao_guan02-qm'],
                            ['laosheng', 'lsxp-Wo_ben_shi-Kong_cheng_ji-qm'],
                            ['laosheng', 'lsxp-Wo_zheng_zai-Kong_cheng_ji04-qm'],
                            ['laosheng', 'lseh-Zi_na_ri-Hong_yang_dong-qm'],
                            ['laosheng', 'lsxp-Huai_nan_wang-Huai_he_ying02-qm'],
                            ['laosheng', 'lsxp-Jiang_shen_er-San_jia_dian02-qm'],
                            ['laosheng', 'lsxp-Wo_zheng_zai-Kong_cheng_ji02-qm'],
                            ['laosheng', 'lsxp-Jiang_shen_er-San_jia_dian01-2-upf'],
                            ['laosheng', 'lseh-Wei_guo_jia-Hong_yang_dong01-lon'],
                            ['laosheng', 'lseh-Tan_Yang_jia-Hong_yang_dong-qm']]

    dev_laosheng_nacta = [['laosheng', 'lseh-Wo_ben_shi-Qiong_lin_yan-qm'],
                          ['laosheng', 'lsxp-Qian_bai_wan-Si_lang_tang_mu01-qm'],
                          ['laosheng', 'lsxp-Quan_qian_sui-Gan_lu_si-qm'],
                          ['laosheng', 'lsxp-Shi_ye_shuo-Ding_jun_shan-qm'], ]

    train_laosheng_primary = [['20171217TianHao/lsxp-Wei_guo_jia-Hong_yang_dong-sizhu', 'teacher'],
                              ['20171217TianHao/lsxp-Jiang_shen_er-San_jia_dian-sizhu', 'teacher'],
                              ['20171217TianHao/lsxp-Ti_lan_xiao_mai-Hong_deng_ji-sizhu_mentougou', 'teacher'],

                              ['20171217TianHao/lsxp-Ti_lan_xiao_mai-Hong_deng_ji-sizhu_mentougou', 'student_01_sizhu'],
                              ['20171217TianHao/lsxp-Ti_lan_xiao_mai-Hong_deng_ji-sizhu_mentougou',
                               'student_02_mentougou'],

                              ['2017121718SongRuoXuan/lsxp-Zhe_yi_feng-Ding_jun_shan-dxjky-sizhu', 'student_01_dxjky'],
                              ['2017121718SongRuoXuan/lsxp-Zhe_yi_feng-Ding_jun_shan-dxjky-sizhu', 'student_01_sizhu'],
                              ['2017121718SongRuoXuan/lsxp-Zhe_yi_feng-Ding_jun_shan-dxjky-sizhu',
                               'student_02_dxjky'], ]
    # ['2017121718SongRuoXuan/lsxp-Zhe_yi_feng-Ding_jun_shan-dxjky-sizhu', 'student_03_dxjky'],
    # ['2017121718SongRuoXuan/lsxp-Zhe_yi_feng-Ding_jun_shan-dxjky-sizhu', 'student_04_dxjky'],
    # ['2017121718SongRuoXuan/lsxp-Zhe_yi_feng-Ding_jun_shan-dxjky-sizhu', 'student_05_dxjky'],
    # ['2017121718SongRuoXuan/lsxp-Zhe_yi_feng-Ding_jun_shan-dxjky-sizhu', 'student_06_mentougou'],]

    dev_laosheng_primary = [['2017121718SongRuoXuan/lsxp-Zhe_yi_feng-Ding_jun_shan-dxjky-sizhu', 'teacher'],
                            ['20171217TianHao/lseh-Wo_men_shi-Zhi_qu-sizhu', 'teacher'],
                            ['20171217TianHao/lsxp-Lin_xing_he_ma-Hong_deng_ji-sizhu', 'teacher'], ]

    test_dan_primary = [['20171211SongRuoXuan/daxp_Qing_zao_qi_lai-Mai_shui-dxjky', 'student01'],
                        ['20171211SongRuoXuan/daxp_Qing_zao_qi_lai-Mai_shui-dxjky', 'student02_first_half'],
                        ['20171211SongRuoXuan/daxp_Qing_zao_qi_lai-Mai_shui-dxjky', 'student02'],
                        ['20171211SongRuoXuan/daxp_Qing_zao_qi_lai-Mai_shui-dxjky', 'student03'],
                        ['20171211SongRuoXuan/daxp_Qing_zao_qi_lai-Mai_shui-dxjky', 'student04'],
                        ['20171211SongRuoXuan/daxp_Qing_zao_qi_lai-Mai_shui-dxjky', 'student05'],
                        ['20171211SongRuoXuan/daxp_Qing_zao_qi_lai-Mai_shui-dxjky', 'student06'],

                        ['20171211SongRuoXuan/daxp-Fei_shi_wo-Hua_tian_cuo-dxjky', 'student01'],
                        ['20171211SongRuoXuan/daxp-Fei_shi_wo-Hua_tian_cuo-dxjky', 'student02'],
                        ['20171211SongRuoXuan/daxp-Fei_shi_wo-Hua_tian_cuo-dxjky', 'student03'],
                        ['20171211SongRuoXuan/daxp-Fei_shi_wo-Hua_tian_cuo-dxjky', 'student04'],

                        ['20171211SongRuoXuan/daxp-Meng_ting_de-Mu_gui_ying_gua_shuai-dxjky', 'student01'],
                        ['20171211SongRuoXuan/daxp-Meng_ting_de-Mu_gui_ying_gua_shuai-dxjky', 'student02'],
                        ['20171211SongRuoXuan/daxp-Meng_ting_de-Mu_gui_ying_gua_shuai-dxjky', 'student03'],
                        ['20171211SongRuoXuan/daxp-Meng_ting_de-Mu_gui_ying_gua_shuai-dxjky', 'student04'],
                        ['20171211SongRuoXuan/daxp-Meng_ting_de-Mu_gui_ying_gua_shuai-dxjky', 'student05'],
                        ['20171211SongRuoXuan/daxp-Meng_ting_de-Mu_gui_ying_gua_shuai-dxjky', 'student06'],
                        ['20171211SongRuoXuan/daxp-Meng_ting_de-Mu_gui_ying_gua_shuai-dxjky', 'student07'],
                        ['20171211SongRuoXuan/daxp-Meng_ting_de-Mu_gui_ying_gua_shuai-dxjky', 'student08'],

                        ['20171211SongRuoXuan/daxp-Wo_jia_di-Hong_deng_ji-dxjky', 'student01'],
                        ['20171211SongRuoXuan/daxp-Wo_jia_di-Hong_deng_ji-dxjky', 'student02'],
                        ['20171211SongRuoXuan/daxp-Wo_jia_di-Hong_deng_ji-dxjky', 'student03'],
                        ['20171211SongRuoXuan/daxp-Wo_jia_di-Hong_deng_ji-dxjky', 'student04'],
                        ['20171211SongRuoXuan/daxp-Wo_jia_di-Hong_deng_ji-dxjky', 'student05'],
                        ['20171211SongRuoXuan/daxp-Wo_jia_di-Hong_deng_ji-dxjky', 'student06'], ]

    test_laosheng_primary = [['20171217TianHao/lsxp-Jiang_shen_er-San_jia_dian-sizhu', 'student_01'],
                             ['20171217TianHao/lsxp-Jiang_shen_er-San_jia_dian-sizhu', 'student_02'],
                             ['20171217TianHao/lsxp-Jiang_shen_er-San_jia_dian-sizhu', 'student_03_1'],
                             ['20171217TianHao/lsxp-Jiang_shen_er-San_jia_dian-sizhu', 'student_03_2'],
                             ['20171217TianHao/lsxp-Jiang_shen_er-San_jia_dian-sizhu', 'student_04_mentougou'],

                             ['20171217TianHao/lsxp-Lin_xing_he_ma-Hong_deng_ji-sizhu', 'student_01'],
                             ['20171217TianHao/lsxp-Lin_xing_he_ma-Hong_deng_ji-sizhu', 'student_02'],
                             ['20171217TianHao/lseh-Wo_men_shi-Zhi_qu-sizhu', 'student_01'],
                             ['20171217TianHao/lseh-Wo_men_shi-Zhi_qu-sizhu', 'student_02'],

                             ['20171217TianHao/lsxp-Wei_guo_jia-Hong_yang_dong-sizhu', 'student_01'],
                             ['20171217TianHao/lsxp-Wei_guo_jia-Hong_yang_dong-sizhu', 'student_02'],
                             ['20171217TianHao/lsxp-Wei_guo_jia-Hong_yang_dong-sizhu', 'student_03'],
                             ['20171217TianHao/lsxp-Wei_guo_jia-Hong_yang_dong-sizhu', 'student_04'],
                             ['20171217TianHao/lsxp-Wei_guo_jia-Hong_yang_dong-sizhu', 'student_05']]

    return train_dan_ss, train_dan_nacta, train_dan_primary, train_laosheng_nacta, train_laosheng_primary, dev_dan_ss, dev_dan_nacta, dev_dan_primary, dev_laosheng_nacta, dev_laosheng_primary, test_dan_primary, test_laosheng_primary


def get_recording_names_jingju_extra():
    extra_primary = [['2017121718SongRuoXuan/lsxp-Zhe_yi_feng-Ding_jun_shan-dxjky-sizhu', 'student_03_dxjky'],
                     ['2017121718SongRuoXuan/lsxp-Zhe_yi_feng-Ding_jun_shan-dxjky-sizhu', 'student_04_dxjky'],
                     ['2017121718SongRuoXuan/lsxp-Zhe_yi_feng-Ding_jun_shan-dxjky-sizhu', 'student_05_dxjky'],
                     ['2017121718SongRuoXuan/lsxp-Zhe_yi_feng-Ding_jun_shan-dxjky-sizhu', 'student_06_mentougou'], ]
    return extra_primary


def get_recording_names_jingju_nacta_2017():
    testNacta2017 = [['20170327LiaoJiaNi', 'lseh-Niang_zi_bu-Sou_gu_jiu-nacta'],  # yes
                     ['20170327LiaoJiaNi', 'lseh-Yi_lun_ming-Wen_zhao_guan-nacta'],  # yes
                     ['20170327LiaoJiaNi', 'lsxp-Jiang_shen_er-San_jia_dian-nacta'],  # yes
                     ['20170327LiaoJiaNi', 'lsxp-Xi_ri_li-Zhu_lian_zhai-nacta'],  # yes
                     ['20170327LiaoJiaNi', 'lsxp-Yi_ma_li-Wu_jia_po-nacta']]  # yes

    trainNacta2017 = [['20170408SongRuoXuan', 'daeh-Yang_yu_huan-Tai_zhen_wai-nacta'],
                      ['20170408SongRuoXuan', 'danbz-Kan_dai_wang-Ba_wang_bie-nacta'],
                      ['20170408SongRuoXuan', 'daspd-Hai_dao_bing-Gui_fei_zui-nacta'],
                      ['20170408SongRuoXuan', 'daxp-Lao_die_die-Yu_zhou_feng-nacta'],
                      ['20170408SongRuoXuan', 'daxp-Su_san_li-Su_san_qi-nacta'],
                      ['20170418TianHao', 'lseh-Jin_zhong_xiang-Shang_tian_tai01-nacta'],
                      ['20170418TianHao', 'lseh-Jin_zhong_xiang-Shang_tian_tai02-nacta'],
                      ['20170418TianHao', 'lseh-Lao_zhang_bu-Wu_pen_ji01-nacta'],
                      ['20170418TianHao', 'lseh-Lao_zhang_bu-Wu_pen_ji02-nacta'],
                      ['20170418TianHao', 'lseh-Niang_zi_bu-Sou_gu_jiu01-nacta'],
                      ['20170418TianHao', 'lseh-Niang_zi_bu-Sou_gu_jiu02-nacta'],
                      ['20170418TianHao', 'lseh-Niang_zi_bu-Sou_gu_jiu03-nacta'],
                      ['20170418TianHao', 'lseh-Tan_yang_jia-Hong_yang_dong-nacta'],
                      ['20170418TianHao', 'lseh-Wei_guo_jia-Hong_yang_dong01-nacta'],
                      ['20170418TianHao', 'lseh-Wei_guo_jia-Hong_yang_dong02-nacta'],
                      ['20170418TianHao', 'lseh-Xin_zhong_you-Wen_zhao_guan01-nacta'],
                      ['20170418TianHao', 'lseh-Xin_zhong_you-Wen_zhao_guan02-nacta'],
                      ['20170418TianHao', 'lseh-Xin_zhong_you-Wen_zhao_guan03-nacta'],
                      ['20170418TianHao', 'lseh-Yi_lun_ming-Wen_zhao_guan01-nacta'],
                      ['20170418TianHao', 'lseh-Yi_lun_ming-Wen_zhao_guan02-nacta'],
                      ['20170418TianHao', 'lsxp-Jiang_shen_er-San_jia_dian-nacta'],
                      ['20170418TianHao', 'lsxp-Liang_guo_jiao-Shi_jie_ting01-nacta'],
                      ['20170418TianHao', 'lsxp-Liang_guo_jiao-Shi_jie_ting02-nacta'],
                      ['20170418TianHao', 'lsxp-Ting_ta_yan-Zhuo_fang_cao01-nacta'],
                      ['20170418TianHao', 'lsxp-Ting_ta_yan-Zhuo_fang_cao02-nacta'],
                      ['20170418TianHao', 'lsxp-Ting_ta_yan-Zhuo_fang_cao03-nacta'],
                      ['20170418TianHao', 'lsxp-Wo_ben_shi-Kong_cheng_ji-nacta'],
                      ['20170418TianHao', 'lsxp-Wo_zheng_zai-Kong_cheng_ji01-nacta'],
                      ['20170418TianHao', 'lsxp-Wo_zheng_zai-Kong_cheng_ji02-nacta'],
                      ['20170418TianHao', 'lsxp-Xi_ri_li-Zhu_lian_zhai-nacta'],
                      ['20170424SunYuZhu', 'daeh-Yi_sha_shi-Suo_lin_nang-nacta'],
                      ['20170424SunYuZhu', 'daxp-Dang_ri_li-Suo_lin_nang-nacta'],
                      ['20170424SunYuZhu', 'daxp-Er_ting_de-Suo_lin_nang_take1-nacta'],
                      ['20170424SunYuZhu', 'daxp-Er_ting_de-Suo_lin_nang_take2-nacta'],
                      ['20170424SunYuZhu', 'daxp-Er_ting_de-Suo_lin_nang_take3-nacta'],
                      ['20170424SunYuZhu', 'daxp-Zhe_cai_shi-Suo_lin_nang-nacta'],
                      ['20170424SunYuZhu', 'daxp-Zhe_cai_shi-Suo_lin_nang_first_half-nacta'],
                      ['20170425SunYuZhu', 'daeh-Wei_kai_yan-Dou_e_yuan-nacta'],
                      ['20170425SunYuZhu', 'daxp-Chui_qiu_ting-Suo_lin_nang-nacta'],
                      ['20170425SunYuZhu', 'daxp-Chui_qiu_ting-Suo_lin_nang_first_line-nacta'],
                      ['20170506LiuHaiLin', 'daeh-Wang_chun_e-San_niang_jiao-ustb'],
                      ['20170506LiuHaiLin', 'daeh-Wei_kai_yan-Dou_e_yuan-ustb'],
                      ['20170506LiuHaiLin', 'daxp-Chun_qiu_ting-Suo_lin_nang-ustb'],
                      ['20170506LiuHaiLin', 'daxp-Dang_ri_li-Suo_lin_nang-ustb'],
                      ['20170506LiuHaiLin', 'daxp-Qiao_lou_shang-Huang_shan_lei-ustb'],
                      ['20170506LiuHaiLin', 'daxp-Yi_sha_shi-Suo_lin_nang-ustb'],
                      ['20170519LongTianMing', 'lseh-Tan_yang_jia-Hong_yang_dong-ustb'],
                      ['20170519LongTianMing', 'lseh-Wei_guo_jia-Hong_yang_dong-ustb'],
                      ['20170519LongTianMing', 'lseh-Yi_lun_ming-Zhuo_fang_cao-ustb'],
                      ['20170519LongTianMing', 'lseh-Zi_na_ri-Hong_yang_dong-ustb'],
                      ['20170519LongTianMing', 'lsxp-Ting_ta_yan-Zhuo_fang_cao-ustb'],
                      ['20170519LongTianMing', 'lsxp-Wo_ben_shi-Kong_cheng_ji-ustb'],
                      ['20170519LongTianMing', 'lsxp-Wo_zheng_zai-Kong_cheng_ji-ustb'],
                      ['20170519XuJingWei', 'lseh-Jin_zhong_xiang-Shang_tian_tai-renmin'],
                      ['20170519XuJingWei', 'lseh-Wei_guo_jia-Hong_yang_dong-renmin'],
                      ['20170519XuJingWei', 'lseh-Wei_kai_yan-Rang_xu_zhou-renmin'],
                      ['20170519XuJingWei', 'lsxp-Huai_nan_wang-Huai_he_ying-renmin'],
                      ['20170519XuJingWei', 'lsxp-Jiang_shen_er-San_jia_dian-renmin'],
                      ['20170519XuJingWei', 'lsxp-Wo_ben_shi-Kong_cheng_ji-renmin'],
                      ['20170519XuJingWei', 'lsxp-Wo_zheng_zai-Kong_cheng_ji-renmin'],
                      ['20170519XuJingWei', 'lsxp-Yi_ma_li-Wu_jia_po-renmin']]
    return trainNacta2017, testNacta2017


def get_kugou_filename():
    clean = ['cheng_du.wav',
             'gang_hao_yu_jian_ni.wav',
             'li_ren_chou.wav',
             'ping_fan_zhi_lu.wav',
             'ti_mian.wav']
    mix = ['ke_xi_bu_shi_ni.wav',
           'tong_zhuo_de_ni.wav',
           'ye_kong_zhong_zui_liang_de_xingxing.wav',
           'yu_jian.wav',
           'zhui_guang_zhe.wav']
    return clean, mix


def get_hansen_filename():
    clean = [
             # 'beautiful_stranger.wav',
             # 'forca.wav',
             'Madonna-Beautiful_Stranger_full_ending',
             'i_kissed_a_girl.wav',
             'clocks_cut.wav',
             'rehab.wav',
             'rolling_in_the_deep.wav',
             'sunrise.wav',
             'this_afternoon.wav',
             'trick_me.wav',
             'umbrella.wav',
             'viva_la_vida.wav'
            ]
    # missing i_kissed_a_girl
    mix = [
           'Madonna-Beautiful_Stranger_full_ending',
           'clocks_cut.wav',
           'i_kissed_a_girl.wav',
           'rehab.wav',
           'rolling_in_the_deep.wav',
           'sunrise.wav',
           'this_afternoon.wav',
           'trick_me.wav',
           'umbrella.wav',
           'viva_la_vida.wav']
    return clean, mix


def get_gracenote_filename():
    mix = ['1979.wav',
           'abba.wav',
           'biggie.wav',
           'daft_punk.wav',
           'hand.wav',
           'jackson.wav',
           'metalica.wav',
           'swift.wav',
           'song1.wav',
           'song2.wav',
           'song3.wav',
           'song4.wav',
           'song5.wav',
           'song6.wav',
           'song7.wav']
    clean = ['song1.wav',
             'song2.wav',
             'song3.wav',
             'song4.wav',
             'song5.wav',
             'song6.wav',
             'song7.wav']
    return clean, mix


def get_mauch_filename():
    mix = ['Abba.KnowingMeKnowingYou.mp3',
           'Bangles.EternalFlame.mp3',
           'Blondie.CallMe.mp3',
           'Duffy.WarwickAvenue.mp3',
           'DuranDuran.OrdinaryWorld.mp3',
           'FranzFerdinand.DoYouWantTo.mp3',
           'Martika.ToySoldiers.mp3',
           'Muse.GuidingLight.mp3',
           'OtisRedding.TheDockOfTheBay.mp3',
           'p082m.mp3',
           'p084m.mp3',
           'Queen.WeAreTheChampions.mp3',
           'RobertPalmer.AddictedToLove.mp3',
           'Santana.BlackMagicWoman.mp3',
           'SimonAndGarfunkel.Cecilia.mp3',
           'TakeThat.BackForGood.mp3',
           'TinaTurner.WhatsLoveGotToDoWithIt.mp3',
           'Toto.Africa.mp3',
           'U2.WithOrWithoutYou.mp3',
           'Zweieck.She.mp3']
    return mix
