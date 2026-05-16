from rest_framework.views import APIView
from rest_framework.response import Response
from rest_framework.permissions import IsAuthenticated
from django.utils import timezone
from django.db.models import Sum
from apps.customers.models import Customer
from apps.orders.models import SalesOrder
from apps.products.models import Product

class DashboardStatsView(APIView):
    permission_classes = [IsAuthenticated]

    def get(self, request):
        today = timezone.now().date()
        
        # 1. Total Customers
        total_customers = Customer.objects.count()
        
        # 2. Total Sales Today (only confirmed orders)
        total_sales_today = SalesOrder.objects.filter(
            order_date__date=today, 
            status=SalesOrder.STATUS_CONFIRMED
        ).aggregate(total=Sum('total_amount'))['total'] or 0
        
        # 3. Stock Running Low (e.g., quantity < 10)
        low_stock_threshold = 10
        low_stock_products = Product.objects.filter(stock_qty__lt=low_stock_threshold).values(
            'sku', 'name', 'stock_qty'
        )
        
        return Response({
            "total_customers": total_customers,
            "total_sales_today": total_sales_today,
            "stock_running_low_count": low_stock_products.count(),
            "stock_running_low_details": list(low_stock_products),
            "date": today
        })
