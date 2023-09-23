from .models import *

class OrderService:
    @staticmethod
    def execute_buy_order(order,user,serializer):
    
        # Check if the buying price matches the last transaction's selling price
        sell_orders = Order.objects.filter(
            # user=user,
            company=order['company'],
            order_type='sell',
            status="P"
        ).order_by('-timestamp').first()
        
        
        if sell_orders and sell_orders.price == order['price']:
            user_portfolio, created = Portfolio.objects.get_or_create(user=user, company=order['company'])
            user_portfolio.quantity += order['qty']
            user_portfolio.save()
            # Perform the transaction logic and record the transaction
            transaction = Transaction.objects.create(
                user=user,
                company=order['company'],
                quantity=order['qty'],
                price=order['price'],
                transaction_type='buy'
            )
            
            order=serializer.save()

            order.status="C"
            order.save()
        else:
            serializer.save()
            
            raise Exception("Buying price doesn't match the last selling price. ")


    @staticmethod
    def execute_sell_order(order,user,serializer):
        if order['order_type'] == 'sell':
            # raise Exception(user)
            user_portfolio = Portfolio.objects.get(user=user, company=order['company'])
            # Check if the selling price matches the last transaction's buying price
     
            last_buy_transaction = Order.objects.filter(
                # user=user,
                company=order['company'],
                order_type='buy',
            ).order_by('-timestamp').first()
            # raise Exception(last_buy_transaction)
            if last_buy_transaction and last_buy_transaction.price == order['price']:
                # raise Exception(user_portfolio.quantity >= order.qty)
                if user_portfolio.quantity >= order['qty']:
                    user_portfolio.quantity -= order['qty']
                    user_portfolio.save()
                    
                    # Check if the selling price matches the last transaction's selling price
                    last_sell_transaction = Order.objects.filter(
                        user=user,
                        company=order.company,
                        order_type='sell',
                        status='P'
                    ).order_by('-timestamp').first()

                    if last_sell_transaction and last_sell_transaction.price == order.price:
                        # Perform the transaction logic and record the transaction
                        transaction = Transaction.objects.create(
                            user=user,
                            company=order.company,
                            quantity=order.qty,
                            price=order.price,
                            transaction_type='sell'
                        )
                        last_buy_transaction.status="C"
                        last_buy_transaction.save()
                        # Any additional transaction-related logic can be added here
                    else:  
                        raise Exception("Selling price doesn't match the last selling price.")
                else:
                    
                    raise Exception("Insufficient quantity in portfolio for selling.")
            else:
                if user_portfolio.quantity >= order['qty']:
                    serializer.save()
                    
                raise Exception("Selling price doesn't match the last buying price. Right Now ")
        else:
            raise Exception("Invalid order type for sell order.")