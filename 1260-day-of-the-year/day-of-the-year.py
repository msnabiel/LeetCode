class Solution(object):
    def dayOfYear(self, date):
        """
        :type date: str
        :rtype: int
        """
        import datetime

        date_obj = datetime.datetime.strptime(date, "%Y-%m-%d")
        return date_obj.timetuple().tm_yday

        