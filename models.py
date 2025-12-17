"""
This module has pydantic models
"""
from enum import Enum
from datetime import datetime, date
from pydantic import BaseModel, Field
from typing import Annotated, List, Optional


class OrderModel(BaseModel):
    """Represents basic order identification and customer information.

    Attributes:
        orderId (str): Unique identifier for the order.
        customerId (str): Unique identifier for the customer.
        customerName (str): Name of the customer who placed the order.
    """
    orderId: Annotated[str, Field(description="order Id", min_length=5)]
    customerId: Annotated[str, Field(description="customer Id", min_length=5)]
    customerName: Annotated[str, Field(description="customer Name", min_length=5)]


class OrderStatus(str, Enum):
    """Enumeration of all supported order statuses.

    This enum is used to track the lifecycle of an order.
    """
    delivered = "delivered"
    cancelled = "cancelled"
    pending = "pending"
    preparing = "preparing"
    out_for_delivery = "out_for_delivery"


class Restaurant(BaseModel):
    """Represents the restaurant from which the order was placed.

    Attributes:
        restaurantId (str | None): Unique ID of the restaurant.
        name (str): Restaurant name.
        location (str): Physical address or locality.
        cuisine (str | None): Optional cuisine description.
        rating (float): Restaurant rating (0–5).
        deliveryTime (str): Estimated delivery time text.
    """
    restaurantId: Annotated[str | None, Field(default=None, alias="restaurantId")] = None
    name: Annotated[str, Field()]
    location: Annotated[str, Field()]
    cuisine: Annotated[str | None, Field(default=None, description="optional comment")] = None
    rating: Annotated[float, Field(ge=0, le=5)]
    deliveryTime: Annotated[str, Field()]  # keeping your original field spelling


class Item(BaseModel):
    """Represents an individual ordered item.

    Attributes:
        name (str): Item name.
        quantity (int): Quantity ordered.
        price (float): Unit price of the item.
        customizations (list[str]): List of custom requests.
    """
    name: Annotated[str, Field()]
    quantity: Annotated[int, Field(ge=1)]
    price: Annotated[float, Field(ge=0)]
    customizations: Annotated[List[str], Field(default_factory=list)]


class Pricing(BaseModel):
    """Represents the detailed price breakdown for an order.

    Attributes:
        itemTotal (float): Total price of items.
        deliveryFee (float): Delivery fee applied.
        platformFee (float): Platform service fee.
        gst (float): GST amount.
        discount (float): Total discount applied.
        totalAmount (float): Final payable amount.
    """
    itemTotal: Annotated[float, Field(ge=0)]
    deliveryFee: Annotated[float, Field(ge=0)]
    platformFee: Annotated[float, Field(ge=0)]
    gst: Annotated[float, Field(ge=0)]
    discount: Annotated[float, Field(ge=0)]
    totalAmount: Annotated[float, Field(ge=0)]


class Payment(BaseModel):
    """Represents payment details of an order.

    Attributes:
        method (str): Payment method used.
        transactionId (str): Unique transaction identifier.
        status (str): Payment status.
    """
    method: Annotated[str, Field()]
    transactionId: Annotated[str, Field(alias="transactionId")]
    status: Annotated[str, Field()]


class DeliveryAddress(BaseModel):
    """Represents the address where the order is delivered.

    Attributes:
        label (str): Address label (e.g., Home, Work).
        address (str): Complete street address.
        city (str): City name.
        pincode (str): 6-digit postal code.
    """
    label: Annotated[str, Field()]
    address: Annotated[str, Field()]
    city: Annotated[str, Field()]
    pincode: Annotated[str, Field(min_length=6, max_length=6)]


class DeliveryPartner(BaseModel):
    """Represents the delivery agent assigned to the order.

    Attributes:
        name (str): Name of the delivery person.
        rating (float): Delivery partner rating (0–5).
        phone (str): Contact number.
    """
    name: Annotated[str, Field()]
    rating: Annotated[float, Field(ge=0, le=5)]
    phone: Annotated[str, Field()]


class Timeline(BaseModel):
    """Represents order lifecycle timestamps.

    Attributes:
        orderPlaced (datetime): When the order was placed.
        restaurantAccepted (datetime): When restaurant accepted.
        foodReady (datetime): When food was prepared.
        outForDelivery (datetime): When rider picked up.
        delivered (datetime): When delivery was completed.
    """
    orderPlaced: Annotated[datetime, Field(alias="orderPlaced")]
    restaurantAccepted: Annotated[datetime, Field(alias="restaurantAccepted")]
    foodReady: Annotated[datetime, Field(alias="foodReady")]
    outForDelivery: Annotated[datetime, Field(alias="outForDelivery")]
    delivered: Annotated[datetime, Field(alias="delivered")]


class Ratings(BaseModel):
    """Represents user ratings and review for an order.

    Attributes:
        food (int): Food quality rating (1–5).
        delivery (int): Delivery service rating (1–5).
        review (str): Written review text.
    """
    food: Annotated[int, Field(ge=1, le=5)]
    delivery: Annotated[int, Field(ge=1, le=5)]
    review: Annotated[str, Field()]


class Order(BaseModel):
    """Represents a complete order structure including items, payment, and delivery.

    Attributes:
        orderId (str): Order identifier.
        customerId (str): Customer identifier.
        customerName (str): Name of customer.
        orderDate (datetime): Timestamp of the order.
        status (OrderStatus): State of the order.
        restaurant (Restaurant): Restaurant details.
        items (List[Item]): List of ordered items.
        pricing (Pricing): Pricing summary.
        payment (Payment): Payment details.
        deliveryAddress (DeliveryAddress): Delivery destination.
        deliveryPartner (DeliveryPartner): Assigned rider.
        timeline (Timeline): Event timestamps.
        ratings (Ratings): User rating and review.
    """
    orderId: Annotated[str, Field(alias="orderId")]
    customerId: Annotated[str, Field(alias="customerId")]
    customerName: Annotated[str, Field(alias="customerName")]
    orderDate: Annotated[datetime, Field(alias="orderDate")]
    status: Annotated[OrderStatus, Field()]
    restaurant: Restaurant
    items: Annotated[List[Item], Field()]
    pricing: Pricing
    payment: Payment
    deliveryAddress: DeliveryAddress
    deliveryPartner: DeliveryPartner
    timeline: Timeline
    ratings: Ratings


class SpiceLevel(str, Enum):
    """Enumeration of user preference spice levels."""
    Mild = "Mild"
    Medium = "Medium"
    Hot = "Hot"


class RecentOrder(BaseModel):
    """Represents summary information about a recent past order.

    Attributes mirror the main Order model, but typically fewer fields
    are used in downstream displays.
    """
    orderId: Annotated[str, Field(alias="orderId")]
    orderDate: Annotated[datetime, Field(alias="orderDate")]
    status: Annotated[OrderStatus, Field()]
    restaurant: Restaurant
    items: Annotated[List[Item], Field()]
    pricing: Pricing
    payment: Payment
    deliveryAddress: DeliveryAddress
    deliveryPartner: DeliveryPartner
    timeline: Timeline
    ratings: Ratings


class Profile(BaseModel):
    """Represents a customer's personal profile information.

    Attributes:
        name (str): Full name.
        email (str): Email address.
        phone (str): Contact number.
        memberSince (date): Date when user joined the platform.
    """
    name: Annotated[str, Field()]
    email: Annotated[str, Field()]
    phone: Annotated[str, Field()]
    memberSince: Annotated[date, Field(alias="memberSince")]


class AccountStats(BaseModel):
    """Represents summarized account statistics for a customer.

    Attributes:
        totalOrders (int): Count of orders placed.
        lifetimeValue (float): Total money spent.
        averageOrderValue (float): Average spend per order.
        favoriteRestaurants (List[str]): Restaurants visited often.
        preferredCuisines (List[str]): User-selected cuisine types.
        savedAddresses (int): Address count saved in profile.
    """
    totalOrders: Annotated[int, Field(ge=0)]
    lifetimeValue: Annotated[float, Field(ge=0)]
    averageOrderValue: Annotated[float, Field(ge=0)]
    favoriteRestaurants: Annotated[List[str], Field(default_factory=list)]
    preferredCuisines: Annotated[List[str], Field(default_factory=list)]
    savedAddresses: Annotated[int, Field(ge=0)]


class Preferences(BaseModel):
    """Represents a user's personal food preferences.

    Attributes:
        dietaryRestrictions (List[str]): Restrictions (e.g., Vegan).
        favoriteItems (List[str]): Frequently ordered items.
        avoidIngredients (List[str]): Ingredients to avoid.
        spiceLevel (SpiceLevel): Preferred spice level.
    """
    dietaryRestrictions: Annotated[List[str], Field(default_factory=list)]
    favoriteItems: Annotated[List[str], Field(default_factory=list)]
    avoidIngredients: Annotated[List[str], Field(default_factory=list)]
    spiceLevel: Annotated[SpiceLevel, Field()]


class Coupon(BaseModel):
    """Represents a coupon assigned to a customer.

    Attributes:
        code (str): Coupon code.
        description (str): Coupon description.
        validUntil (date): Expiry date.
    """
    code: Annotated[str, Field()]
    description: Annotated[str, Field()]
    validUntil: Annotated[date, Field(alias="validUntil")]


class LoyaltyRewards(BaseModel):
    """Represents loyalty reward details for a customer.

    Attributes:
        currentPoints (int): Active loyalty points.
        pointsToNextReward (int): Points needed for next reward.
        couponsAvailable (List[Coupon]): List of active coupons.
    """
    currentPoints: Annotated[int, Field(ge=0)]
    pointsToNextReward: Annotated[int, Field(ge=0)]
    couponsAvailable: Annotated[List[Coupon], Field(default_factory=list)]


class Customer(BaseModel):
    """Represents a complete customer entity with all account information.

    Attributes:
        customerId (str): Unique customer ID.
        profile (Profile): Personal profile details.
        accountStats (AccountStats): Statistical summary.
        recentOrders (List[RecentOrder]): List of latest orders.
        preferences (Preferences): Food preferences.
        loyaltyRewards (LoyaltyRewards): Rewards and coupons.
    """
    customerId: Annotated[str, Field(alias="customerId")]
    profile: Profile
    accountStats: AccountStats
    recentOrders: Annotated[List[RecentOrder], Field(default_factory=list)]
    preferences: Preferences
    loyaltyRewards: LoyaltyRewards
