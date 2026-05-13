from preprocessing import avg_price, max_price, min_price, year_counts

class StatService:
    def get_stats(self):
        return {
            "평균가격": int(avg_price),
            "최고가격": int(max_price),
            "최저가격": int(min_price),
            "최다출판연도": int(year_counts.idxmax())
        }

# 서비스 객체 생성
stat_service = StatService()
