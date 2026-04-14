"""Commerce views — split into customer-facing and seller dashboard."""
from apps.commerce.views.customer import (  # noqa: F401
    AddToCartView,
    CartView,
    CheckoutView,
    OrderConfirmationView,
    RemoveCartItemView,
    ShopView,
    ProductDetailView,
    UpdateCartItemView,
)
from apps.commerce.views.seller import (  # noqa: F401
    DashboardHomeView,
    OrderDetailView,
    OrdersListView,
    ProductCreateView,
    ProductDeleteView,
    ProductUpdateView,
    ProductsListView,
    VariantCreateView,
    VariantDeleteView,
    VariantUpdateView,
)
