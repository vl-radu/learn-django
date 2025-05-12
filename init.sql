START TRANSACTION;

-- Create model PromotionEvent
CREATE TABLE inventory_promotionevent (
    id INT NOT NULL AUTO_INCREMENT PRIMARY KEY,
    name VARCHAR(50) NOT NULL UNIQUE,
    price_reduction INT NOT NULL,
    start_date DATETIME NOT NULL,
    end_date DATETIME NOT NULL
);

-- Create model User
CREATE TABLE inventory_user (
    id INT NOT NULL AUTO_INCREMENT PRIMARY KEY,
    username VARCHAR(50) NOT NULL UNIQUE,
    email VARCHAR(255) NOT NULL UNIQUE,
    password VARCHAR(60) NOT NULL
);

-- Create model Category
CREATE TABLE inventory_category (
    id INT NOT NULL AUTO_INCREMENT PRIMARY KEY,
    name VARCHAR(50) NOT NULL UNIQUE,
    slug VARCHAR(55) NOT NULL UNIQUE,
    is_active BOOLEAN NOT NULL,
    level SMALLINT NOT NULL,
    parent_id INT,
    FOREIGN KEY (parent_id) REFERENCES inventory_category(id)
);

-- Create model Product
CREATE TABLE inventory_product (
    id INT NOT NULL AUTO_INCREMENT PRIMARY KEY,
    name VARCHAR(50) NOT NULL UNIQUE,
    slug VARCHAR(55) NOT NULL UNIQUE,
    description TEXT,
    is_digital BOOLEAN NOT NULL,
    is_active BOOLEAN NOT NULL,
    created_at DATETIME NOT NULL,
    updated_at DATETIME NOT NULL,
    price DECIMAL(10,2) NOT NULL,
    category_id INT NOT NULL,
    FOREIGN KEY (category_id) REFERENCES inventory_category(id)
);

-- Create model StockManagement
CREATE TABLE inventory_stockmanagement (
    id INT NOT NULL AUTO_INCREMENT PRIMARY KEY,
    quantity INT NOT NULL,
    last_checked_at DATETIME NOT NULL,
    product_id INT NOT NULL UNIQUE,
    FOREIGN KEY (product_id) REFERENCES inventory_product(id)
);

-- Create model Order
CREATE TABLE inventory_order (
    id INT NOT NULL AUTO_INCREMENT PRIMARY KEY,
    created_at DATETIME NOT NULL,
    updated_at DATETIME NOT NULL,
    user_id INT NOT NULL,
    FOREIGN KEY (user_id) REFERENCES inventory_user(id)
);

-- Create model OrderProduct
CREATE TABLE inventory_orderproduct (
    id INT NOT NULL AUTO_INCREMENT PRIMARY KEY,
    quantity INT NOT NULL,
    order_id INT NOT NULL,
    product_id INT NOT NULL,
    FOREIGN KEY (order_id) REFERENCES inventory_order(id),
    FOREIGN KEY (product_id) REFERENCES inventory_product(id)
);

-- Create model ProductPromotionEvent
CREATE TABLE inventory_productpromotionevent (
    id INT NOT NULL AUTO_INCREMENT PRIMARY KEY,
    product_id INT NOT NULL,
    promotion_event_id INT NOT NULL,
    FOREIGN KEY (product_id) REFERENCES inventory_product(id),
    FOREIGN KEY (promotion_event_id) REFERENCES inventory_promotionevent(id)
);

COMMIT;
