# File generated from our OpenAPI spec by Stainless. See CONTRIBUTING.md for details.

from typing import Dict, List, Union, Optional
from typing_extensions import TypeAlias

from pydantic import Field as FieldInfo

from .brand import Brand
from .image import Image
from .offer import Offer
from .offers import Offers
from .rating import Rating
from .review import Review
from .._models import BaseModel
from .audience import Audience
from .category import Category
from .promotion import Promotion
from .color_info import ColorInfo
from .organization import Organization
from .video_object import VideoObject
from .three_d_model import ThreeDModel
from .aggregate_offer import AggregateOffer
from .breadcrumb_list import BreadcrumbList
from .fulfillment_info import FulfillmentInfo
from .product_enrichment import ProductEnrichment

__all__ = [
    "SearchToolOutput",
    "Product",
    "ProductAdditionalAttributes",
    "ProductBrand",
    "ProductHasVariant",
    "ProductHasVariantAdditionalAttributes",
    "ProductHasVariantBrand",
    "ProductHasVariantOffers",
    "ProductOffers",
]


class ProductAdditionalAttributes(BaseModel):
    numbers: Optional[List[float]] = None
    """Number attributes"""

    text: Optional[List[str]] = None
    """Text attributes"""


ProductBrand: TypeAlias = Union[Brand, Organization, None]


class ProductHasVariantAdditionalAttributes(BaseModel):
    numbers: Optional[List[float]] = None
    """Number attributes"""

    text: Optional[List[str]] = None
    """Text attributes"""


ProductHasVariantBrand: TypeAlias = Union[Brand, Organization, None]

ProductHasVariantOffers: TypeAlias = Union[Offer, AggregateOffer, Offers, None]


class ProductHasVariant(BaseModel):
    id: Optional[str] = None
    """Product identifier.

    Can be the identifier of a SKU as well. It should not be confused with any of
    the GTIN\\** numbers.
    """

    additional_attributes: Optional[Dict[str, Optional[ProductHasVariantAdditionalAttributes]]] = None
    """Extra product attributes."""

    audience: Optional[Audience] = None
    """Target group associated with the product."""

    brand: Optional[ProductHasVariantBrand] = None
    """The brand or organization associated with the product."""

    breadcrumb_list: Optional[BreadcrumbList] = FieldInfo(alias="breadcrumbList", default=None)
    """Breadcrumb list of the product."""

    catalog: Optional[str] = None
    """Catalog name, or ecommerce site name. Eg: Macys, sephora etc"""

    categories: Optional[List[Category]] = None
    """Product categories."""

    color_info: Optional[ColorInfo] = None
    """Color of the product."""

    description: Optional[str] = None
    """Product description."""

    dimensions: Optional[str] = None
    """The dimensions of the product."""

    enrichment: Optional[ProductEnrichment] = None
    """Enrichment information for the product.

    This is generated by the product information enrichment service.
    """

    extra_text: Optional[str] = None
    """Extra text field for additional information. Extracted from the web-page"""

    fit: Union[str, List[str], None] = None
    """The fit of the product."""

    fulfillment_info: Optional[List[FulfillmentInfo]] = None
    """Fulfillment information."""

    gtin: Optional[str] = None
    """Global Trade Item Number.

    a unique identifier used to recognize and track products globally in ecommerce,
    retail, and supply chains. It ensures that products are correctly identified
    across different marketplaces, point-of-sale (POS) systems, and logistics
    networks. Should not be confused with product or SKU id.
    """

    image: Optional[Image] = None
    """Primary product image."""

    images: Optional[List[Image]] = None
    """Product image."""

    language_code: Optional[str] = None
    """Language of the name and description."""

    materials: Optional[List[str]] = None
    """Material of the product."""

    name: Optional[str] = None
    """Full name or title of the product."""

    offers: Optional[ProductHasVariantOffers] = None
    """Offer or AggregateOffer for the product."""

    organization: Optional[Organization] = None
    """Schema.org model for Organization."""

    patterns: Optional[List[str]] = None
    """Pattern or graphic print of the product."""

    primary_product_id: Optional[str] = None
    """
    Used by Variant to refer to the productGroupID of the productGroup in which the
    product belongs
    """

    promotions: Optional[List[Promotion]] = None
    """Promotions applied to the product."""

    rating: Optional[Rating] = None
    """Product rating."""

    review: Optional[List[Review]] = None
    """List of reviews for the product."""

    sizes: Optional[List[str]] = None
    """Size of the product.

    A SKU has a single size. A product group can have a list of them.
    """

    tags: Optional[List[str]] = None
    """Custom tags associated with the product."""

    three_d_model: Optional[List[ThreeDModel]] = None
    """3D model of the product."""

    type: Optional[str] = None
    """The schema type."""

    url: Optional[str] = None
    """Canonical URL linking to the product detail page."""

    videos: Optional[List[VideoObject]] = None
    """Product video/videos."""


ProductOffers: TypeAlias = Union[Offer, AggregateOffer, Offers, None]


class Product(BaseModel):
    uuid: str

    id: Optional[str] = None
    """Product identifier.

    Can be the identifier of a SKU as well. It should not be confused with any of
    the GTIN\\** numbers.
    """

    additional_attributes: Optional[Dict[str, Optional[ProductAdditionalAttributes]]] = None
    """Extra product attributes."""

    audience: Optional[Audience] = None
    """Target group associated with the product."""

    brand: Optional[ProductBrand] = None
    """The brand or organization associated with the product."""

    brand_name: Optional[str] = None

    breadcrumb_list: Optional[BreadcrumbList] = FieldInfo(alias="breadcrumbList", default=None)
    """Breadcrumb list of the product."""

    catalog: Optional[str] = None
    """Catalog name, or ecommerce site name. Eg: Macys, sephora etc"""

    categories: Optional[List[Category]] = None
    """Product categories."""

    color_info: Optional[ColorInfo] = None
    """Color of the product."""

    current_price: Optional[float] = None

    description: Optional[str] = None
    """Product description."""

    dimensions: Optional[str] = None
    """The dimensions of the product."""

    enrichment: Optional[ProductEnrichment] = None
    """Enrichment information for the product.

    This is generated by the product information enrichment service.
    """

    extra_text: Optional[str] = None
    """Extra text field for additional information. Extracted from the web-page"""

    fit: Union[str, List[str], None] = None
    """The fit of the product."""

    fulfillment_info: Optional[List[FulfillmentInfo]] = None
    """Fulfillment information."""

    gtin: Optional[str] = None
    """Global Trade Item Number.

    a unique identifier used to recognize and track products globally in ecommerce,
    retail, and supply chains. It ensures that products are correctly identified
    across different marketplaces, point-of-sale (POS) systems, and logistics
    networks. Should not be confused with product or SKU id.
    """

    has_variant: Optional[List[ProductHasVariant]] = FieldInfo(alias="hasVariant", default=None)
    """Indicates a list of Products that are variants of this ProductGroup"""

    image: Optional[Image] = None
    """Primary product image."""

    images: Optional[List[Image]] = None
    """Product image."""

    language_code: Optional[str] = None
    """Language of the name and description."""

    materials: Optional[List[str]] = None
    """Material of the product."""

    name: Optional[str] = None
    """Full name or title of the product."""

    offers: Optional[ProductOffers] = None
    """Offer or AggregateOffer for the product."""

    organization: Optional[Organization] = None
    """Schema.org model for Organization."""

    original_price: Optional[float] = None

    patterns: Optional[List[str]] = None
    """Pattern or graphic print of the product."""

    primary_product_id: Optional[str] = None
    """
    Used by Variant to refer to the productGroupID of the productGroup in which the
    product belongs
    """

    product_group_id: Optional[str] = FieldInfo(alias="productGroupID", default=None)
    """ID of the product group."""

    promotions: Optional[List[Promotion]] = None
    """Promotions applied to the product."""

    rating: Optional[Rating] = None
    """Product rating."""

    review: Optional[List[Review]] = None
    """List of reviews for the product."""

    sizes: Optional[List[str]] = None
    """Size of the product.

    A SKU has a single size. A product group can have a list of them.
    """

    tags: Optional[List[str]] = None
    """Custom tags associated with the product."""

    three_d_model: Optional[List[ThreeDModel]] = None
    """3D model of the product."""

    type: Optional[str] = None
    """The schema type."""

    url: Optional[str] = None
    """Canonical URL linking to the product detail page."""

    varies_by: Optional[List[str]] = FieldInfo(alias="variesBy", default=None)
    """
    Indicates the property or properties by which the variants in a ProductGroup
    vary, e.g. their size, color, etc.
    """

    videos: Optional[List[VideoObject]] = None
    """Product video/videos."""


class SearchToolOutput(BaseModel):
    products: List[Product]
    """The list of product groups that match the input search query and filters."""

    total_found: int
    """The total number of products returned by the search."""

    error: Optional[str] = None
    """The error message if the search query is invalid or the search failed.

    The products field will be an empty list if the search fails and total_found
    will be 0.
    """
