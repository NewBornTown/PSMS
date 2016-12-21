# -*- coding: utf-8 -*-
from main import db


# 用户和用户组关联表
user_group = db.Table('users_group',
                      # db.Column(db.Integer, primary_key=True),
                      db.Column('users_id', db.Integer, db.ForeignKey('users.id')),
                      db.Column('group_id', db.Integer, db.ForeignKey('group.id'))
                      )
# 用户组和权限关联表
group_permissions = db.Table('group_permissions',
                             # db.Column(db.Integer, primary_key=True),
                             db.Column('group_id', db.Integer, db.ForeignKey('group.id')),
                             db.Column('permissions_id', db.Integer, db.ForeignKey('permissions.id'))
                             )
# 用户和权限关联表
user_permissions = db.Table('user_permissions',
                            # db.Column(db.Integer, primary_key=True),
                            db.Column('users_id', db.Integer, db.ForeignKey('users.id')),
                            db.Column('permissions_id', db.Integer, db.ForeignKey('permissions.id'))
                            )


# 用户表
class Users(db.Model):
    __tablename__ = 'users'
    id = db.Column(db.Integer, primary_key=True)
    name = db.Column(db.String(100), nullable=False)
    email = db.Column(db.String(100), nullable=False)
    passwd = db.Column(db.String(100), nullable=False)
    phone = db.Column(db.String(100), nullable=False)
    group = db.relationship('Group', secondary=user_group,
                              backref=db.backref('users', lazy='dynamic'),
                              lazy='dynamic')
    permissions = db.relationship('Permissions', secondary=user_permissions,
                            backref=db.backref('users', lazy='dynamic'),
                            lazy='dynamic')
    def __init__(self, name, email, passwd, phone):
        self.name = name
        self.email = email
        self.passwd = passwd
        self.phone = phone

    def __repr__(self):
        users = ''
        users += 'name: %s\n' % (self.name)
        return users


# 用户组的表
class Group(db.Model):
    __tablename__ = 'group'
    id = db.Column(db.Integer, primary_key=True)
    name = db.Column(db.String(100), nullable=False)
    permissions = db.relationship('Permissions', secondary=group_permissions,
                            backref=db.backref('group', lazy='dynamic'),
                            lazy='dynamic')

    def __init__(self, name):
        self.name = name


# 权限表
class Permissions(db.Model):
    __tablename__ = 'permissions'
    id = db.Column(db.Integer, primary_key=True)
    name = db.Column(db.String(100), nullable=False)


    def __init__(self, name):
        self.name = name


# 客户表
class Customers(db.Model):
    __tablename__ = 'customers'
    id = db.Column(db.Integer, primary_key=True)
    customer_code = db.Column(db.String(100), nullable=False, unique=True)
    company_name = db.Column(db.String(100), nullable=False, unique=True)
    company_address = db.Column(db.String(100), nullable=False)
    comment = db.Column(db.String(100), nullable=False)

    def __init__(self, customer_code, company_name, company_address, comment):
        self.customer_code = customer_code
        self.company_name = company_name
        self.company_address = company_address
        self.comment = comment

    def __repr__(self):
        customer_code = ''
        customer_code += 'name: %s\n' % (self.customer_code)
        return customer_code


class Offer(db.Model):
    __tablename__ = 'offer'
    id = db.Column(db.Integer, primary_key=True)
    user_id = db.Column(db.Integer, db.ForeignKey('users.id'))  # 销售
    # advertiser_id = db.Column(db.Integer, db.ForeignKey('advertiser.id'))
    status = db.Column(db.String(100), default='active')
    contract_type = db.Column(db.String(100), default='cpa')  # 合同模式
    contract_num = db.Column(db.String(100), nullable=False)  # 合同编号
    contract_scale = db.Column(db.Integer, default=0)  # 合同模式为服务费时存在
    os = db.Column(db.String(100), nullable=False)  # 操作系统　
    package_name = db.Column(db.String(100), nullable=False)  # 包名
    app_name = db.Column(db.String(100), nullable=False)
    app_type = db.Column(db.String(100), nullable=False)
    preview_link = db.Column(db.String(100), nullable=False)
    track_link = db.Column(db.String(100), nullable=False)
    material = db.Column(db.Boolean, default=False)
    startTime = db.Column(db.String(100), nullable=False)  # 投放开始时间
    endTime = db.Column(db.String(100), nullable=False)  # 投放结束时间
    platform = db.Column(db.String(100), nullable=False)  # 投放平台
    country = db.Column(db.String(100), nullable=False)  # 投放国家
    price = db.Column(db.Float, default=0)  # 投放单价
    daily_budget = db.Column(db.Float, default=0)  # 最高日预算
    daily_type = db.Column(db.String(100), default='install')  # 最高日预算的类型
    total_budget = db.Column(db.Float, default=0)  # 最高总预算
    total_type = db.Column(db.String(100), default='cost')  # 最高总预算的类型
    distribution = db.Column(db.String(100), nullable=False)  # 预算分配
    authorized = db.Column(db.String(100), nullable=False)  # 授权账户
    named_rule = db.Column(db.String(100), nullable=False)  # 命名规则
    KPI = db.Column(db.String(100), nullable=False)  # kpi要求
    settlement = db.Column(db.String(100), nullable=False)  # 结算标准
    period = db.Column(db.String(100), nullable=False)  # 账期
    remark = db.Column(db.String(100), nullable=False)  # 备注
    email_time = db.Column(db.Float, nullable=False)  # 邮件发送时间
    email_users = db.Column(db.String(100), nullable=False)  # 邮件收件人
    email_tempalte = db.Column(db.Integer, nullable=False)  # 报告模版
    createdTime = db.Column(db.String(100), nullable=False)

    def __init__(self, user_id, status, contract_type, contract_num, contract_scale, os, package_name, app_name,
                 app_type, preview_link, track_link, material, startTime, endTime, platform, country, price,
                 daily_budget, daily_type, total_budget, total_type, distribution, authorized, named_rule, KPI,
                 settlement, period, remark, email_time, email_users, email_tempalte, createdTime):
        self.user_id = user_id
        # self.advertiser_id = advertiser_id
        self.status = status
        self.contract_type = contract_type
        self.contract_num = contract_num
        self.contract_scale = contract_scale
        self.os = os
        self.package_name = package_name
        self.app_name = app_name
        self.app_type = app_type
        self.preview_link = preview_link
        self.track_link = track_link
        self.material = material
        self.startTime = startTime
        self.endTime = endTime
        self.platform = platform
        self.country = country
        self.price = price
        self.daily_budget = daily_budget
        self.daily_type = daily_type
        self.total_budget = total_budget
        self.total_type = total_type
        self.distribution = distribution
        self.authorized = authorized
        self.named_rule = named_rule
        self.KPI = KPI
        self.settlement = settlement
        self.period = period
        self.remark = remark
        self.email_time = email_time
        self.email_users = email_users
        self.email_tempalte = email_tempalte
        self.createdTime = createdTime

    def __repr__(self):
        return '<Offer {}>'.format(self.id)


class History(db.Model):
    __tablename__ = 'history'
    id = db.Column(db.Integer, primary_key=True)
    offer_id = db.Column(db.Integer, db.ForeignKey('offer.id'))
    user_id = db.Column(db.Integer, db.ForeignKey('users.id'))
    type = db.Column(db.String(100), default='default')
    createdTime = db.Column(db.String(100), nullable=False)
    country = db.Column(db.String(100), nullable=False)
    country_price = db.Column(db.Float, nullable=True)
    price = db.Column(db.Float, default=0)
    daily_budget = db.Column(db.Float, default=0)  # 最高日预算
    total_type = db.Column(db.String(100), default='cost')
    total_budget = db.Column(db.Float, default=0)
    total_type = db.Column(db.String(100), default='cost')  # 最高总预算的类型
    KPI = db.Column(db.String(100), nullable=False)  # kpi要求

    def __init__(self, offer_id, user_id, type, createdTime, country, country_price, price, daily_budget, total_type,
                 total_budget, KPI):
        self.offer_id = offer_id
        self.user_id = user_id
        self.type = type
        self.createdTime = createdTime
        self.country = country
        self.country_price = country_price
        self.price = price
        self.daily_budget = daily_budget
        self.total_type = total_type
        self.total_budget = total_budget
        self.KPI = KPI

    def __repr__(self):
        return '<History {}>'.format(self.id)
