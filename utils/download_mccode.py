from baidupcs_py.baidupcs import BaiduPCSApi
from baidupcs_py.commands.rapid_upload import rapid_upload
import yaml
from tqdm import tqdm

bduss = 'mJUVHYwR3M0aGRDTU05RHpad0Mxd2lxSzdTLUdMUEdBaFhuQmJVaFJkdGw4cHBqSVFBQUFBJCQAAAAAAAAAAAEAAAC-JAabaG9tZbTzzf7J2TY2AAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAGVlc2NlZXNjS'
cookies_string = 'XFI=ff932f15-5c5e-6380-b51e-4a2d93ed94f5; XFCS=98C5FA1458E040BB568A7C595AD19594EB2B5BC0CFD8244731BDCC1D475611CB; XFT=BFrmFqgC460Y6xABKZa63C8RGelWO5O69yKLoK+4ZU4=; BAIDUID=8F76B059F39561050C647FE396EBAF67:FG=1; csrfToken=qZ_EFl_9gkKHa8mJWPuTLXbf; BDUSS=mJUVHYwR3M0aGRDTU05RHpad0Mxd2lxSzdTLUdMUEdBaFhuQmJVaFJkdGw4cHBqSVFBQUFBJCQAAAAAAAAAAAEAAAC-JAabaG9tZbTzzf7J2TY2AAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAGVlc2NlZXNjS; BDUSS_BFESS=mJUVHYwR3M0aGRDTU05RHpad0Mxd2lxSzdTLUdMUEdBaFhuQmJVaFJkdGw4cHBqSVFBQUFBJCQAAAAAAAAAAAEAAAC-JAabaG9tZbTzzf7J2TY2AAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAGVlc2NlZXNjS; BIDUPSID=8F76B059F39561050C647FE396EBAF67; PSTM=1668514323; PANWEB=1; H_WISE_SIDS=219946_231979_234927_219623_237835_232777_235174_239479_234020_230584_131861_234208_232244_219563_238804_237874_234426_240016_234307_236536_240663_240447_240466_241207_239492_240034_216841_227932_213359_229976_211986_214794_235967_238511_223064_219942_213034_228650_204919_241246_238073_230288_241505_242024_240734_241780_242083_242158_242380_242370_241687_241892_241699_242465_242548_242513_242620_242489_242421_242753_242542_238267_242626_241964_242498_241748_242335_239308_240999_243408_110085_227870_237794_243508_236312_243593_243842_243848_243706_243855_243850_242128_243877_243123_244039_244272_244323_244252_244409_240597_244006_244446_244476_243658; H_WISE_SIDS_BFESS=219946_231979_234927_219623_237835_232777_235174_239479_234020_230584_131861_234208_232244_219563_238804_237874_234426_240016_234307_236536_240663_240447_240466_241207_239492_240034_216841_227932_213359_229976_211986_214794_235967_238511_223064_219942_213034_228650_204919_241246_238073_230288_241505_242024_240734_241780_242083_242158_242380_242370_241687_241892_241699_242465_242548_242513_242620_242489_242421_242753_242542_238267_242626_241964_242498_241748_242335_239308_240999_243408_110085_227870_237794_243508_236312_243593_243842_243848_243706_243855_243850_242128_243877_243123_244039_244272_244323_244252_244409_240597_244006_244446_244476_243658; STOKEN=47e7ad5b0bd096561bd8e20b600eb2d675bb4b401ad323188e9e730c461b8318; newlogin=1; BDRCVFR[feWj1Vr5u3D]=I67x6TjHwwYf0; delPer=0; PSINO=5; BAIDUID_BFESS=8F76B059F39561050C647FE396EBAF67:FG=1; ZFY=Q:B9TwGs2fzTAEd7PQx9MNDiU3qw:AMIvN12y0Rsjbifg:C; H_PS_PSSID=38186_36549_37514_37911_37861_38173_38290_38231_36807_37925_38314_38324_38285_37900_26350_37957_22160_37881; ZD_ENTRY=google; Hm_lvt_fa0277816200010a74ab7d2895df481b=1678448998; Hm_lpvt_fa0277816200010a74ab7d2895df481b=1678448998; BDCLND=cYV%2FSkvtOfqWfN6v3MwNpwrq22%2Bj2oS1oxPumLYex8U%3D; ___wk_scode_token=uEfRx2rYUN0OX6in6GGEszJ4n2HtVtztUc2NSYUMr6s%3D; Hm_lvt_7a3960b6f067eb0085b7f96ff5e660b0=1678581285; Hm_lpvt_7a3960b6f067eb0085b7f96ff5e660b0=1678581285; PANPSC=17511105091479159520%3ACmYbeee4quUcmyql2Po5ajuv496EomYGm3IMNKjGNgvmBHEtpP4IYVHh9%2B0QKjNvz81ttRoL0tBKQ4Dasb9%2FZsriRVUCnprRssns6AvA%2FXgh7IX89yGaj0mLLbwvPTIG4RF1wO0ONuLR4SeWmT6baF9K9yVk1uvA4i2i1JdCg%2BQoj3hBKvZymPgT7Eg6UyTb; ndut_fmt=CF6094B672EE11B149A9EA4DBB84E14F17638390905DB3653F2EC310E30275DB; ab_sr=1.0.1_MzAxN2E0ZGVkZGUwNjk4ODNkNjNiYTE0M2RlOTIzM2I0YTMxYmQyMTM0ODFkZWFiOGNhYzJlNzc4MTFmYzI4ODNhZjhjNWU5OGZiMGIyMjZmNWQ4MDJlMzU4ZmY0MzAzN2JkZTQ3ODg4NDZiN2MzNTdjZDRiNmI4NDhmZmQwZjdmNDdiNDYwY2ZjYmFmMmU2ZGE5OTZhYjcxOGZmNjhmNTI2MGUyYmUyMjNhNGNiNmFkMGVmNjVkNWFhMmEwZWZl'

books_info_file = 'valid_books_info.yaml'
remote_dir = '/我的资源/特殊教育/资源/nokidsnocry/doing/'

def get_cookies():
    cookies_dict = {}
    cookies_list = cookies_string.split('; ')
    for cookie in cookies_list:
        cookie_list = cookie.split('=', 1)
        cookies_dict[cookie_list[0]] = cookie_list[1]
    return cookies_dict
    

def read_books_info():
    with open(books_info_file, 'r', encoding='utf-8') as f:
        data = f.read()
        data = yaml.safe_load(data)
        return data 


def download_books(data):
    api = BaiduPCSApi(bduss=bduss, cookies=get_cookies())
    for item in tqdm(data, desc='Processing...'):
        book_mccode = item['book_mccode'] 
        book_mccode_suffix = book_mccode.rsplit('.', 1)[1]
        book_filename = item['book_name'] + '_' + item['book_sscode'] + '.' + book_mccode_suffix
        rapid_upload(api=api, remotedir=remote_dir, link=book_mccode, filename=book_filename)


def main():
    data = read_books_info()
    download_books(data)


if __name__ == '__main__':
    main()
